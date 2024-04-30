import sounddevice as sd
import numpy as np
import time
import tempfile
import os
import asyncio

from kink import inject
from config import Config
from data import Data
from logging import Logging
from models import AppState
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
from util import cleanOutputText
from threading import Thread


@inject
class Audio:

    _thread = None
    _textToSpeechQueue = asyncio.Queue()
    _shutdown_event = asyncio.Event()

    def __init__(self, config: Config, data: Data, logging: Logging):
        self._data = data
        self._config = config
        self._logging = logging
        # async tasks
        self._thread = Thread(target=self._runAsyncTasks)
        self._thread.start()

    def recordAudio(self):
        audioData = []
        self._data.changeAppState(AppState.RECORDING_INPUT)
        blockDuration = self._config.RECORDING_BLOCK_DURATION
        duration = self._config.RECORDING_DURATION
        sampleRate = self._config.RECORDING_SAMPLE_RATE

        def callback(inData, frames, time, status):
            nonlocal audioData
            if self._data.appState == AppState.RECORDING_INPUT:
                audioData.append(inData.copy())

        with sd.InputStream(
            callback=callback,
            samplerate=sampleRate,
            channels=1,
            blocksize=int(sampleRate * blockDuration),
        ):
            while (
                self._data.appState == AppState.RECORDING_INPUT
                and len(audioData) * blockDuration < duration
            ):
                sd.sleep(int(blockDuration * 1000))

        audioData = np.concatenate(audioData, axis=0)
        return audioData, sampleRate

    def transcribeAudioToText(self, audioData, sampleRate):
        startTime = time.time()
        tempDir = "./input/"
        os.makedirs(tempDir, exist_ok=True)
        tempFilePath = tempfile.mktemp(suffix=".wav", dir=tempDir)
        try:
            write(tempFilePath, sampleRate, audioData)
            segments, _ = WhisperModel(
                self._config.WHISPER_MODEL_SIZE,
                device=self._config.WHISPER_DEVICE,
                compute_type=self._config.WHISPER_COMPUTE_TYPE,
            ).transcribe(tempFilePath)

            transcript = " ".join(segment.text for segment in segments)
            self._logging.logUser("User: " + transcript)
            endTime = time.time()
            duration = startTime - endTime
            self._logging.logInfo(f"Transcription: + {duration:.2f} seconds")
            return transcript
        except Exception as e:
            self._logging.logError(f"Error during transcription: {e}")
        finally:
            os.remove(tempFilePath)

    def shutDownTreads(self):
        self._thread.join()
        self._shutdown_event.set()

    def addToAsyncTextToSpeechQueue(self, text: str):
        self._textToSpeechQueue.put_nowait(text)

    async def _playAudio(self):
        text = await self._textToSpeechQueue.get()
        os.system(
            "say -v  com.apple.speech.synthesis.voice.joelle " + cleanOutputText(text)
        )
        await asyncio.sleep(0.5)

    async def _textToSpeechConsumer(self):
        while True:
            text = await self._textToSpeechQueue.get()
            await self._processTextToSpeech(text)
            self._textToSpeechQueue.task_done()

    async def _processTextToSpeech(self, text: str):
        await asyncio.sleep(0.1)
        # we will include cloud based text to speech here in the future

    async def _addAsyncTasks(
        self,
    ):
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:  # No running event loop
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        consumer_task = loop.create_task(self._textToSpeechConsumer())
        play_task = loop.create_task(self._playAudio())
        return consumer_task, play_task
      

    def _runAsyncTasks(self):
        # Set up the event loop and run the async tasks
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self._addAsyncTasks())

        try:
            loop.run_until_complete(self._shutdown_event.wait())
        finally:
            loop.close()
