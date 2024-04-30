import sounddevice as sd
import numpy as np
import time
import tempfile
import os

from kink import inject
from config import Config
from data import Data
from log import Logging
from models import AppState
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
from util import cleanOutputText
from threading import Thread


@inject
class Audio:

    def __init__(self, config: Config, data: Data, logging: Logging):
        self._data = data
        self._config = config
        self._logging = logging

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

    def playAudio(self, text):
        os.system(
            f"say -v {self._config.LOCAL_TTS_VOICE} -r {self._config.LOCAL_TTS_RATE} " + cleanOutputText(text)
        )
