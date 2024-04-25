from config import Config
from data import Data
from models import AppState
import sounddevice as sd
import numpy as np


class Audio:

    def __init__(self, data: Data, config: Config):
        self.data = data
        self.config = config

    def recordAudio(self):
        audioData = []
        self.data.changeAppState(AppState.RECORDING_INPUT)
        blockDuration = self.config.RECORDING_BLOCK_DURATION
        duration = self.config.RECORDING_DURATION
        sampleRate = self.config.RECORDING_SAMPLE_RATE

        def callback(inData, frames, time, status):
            nonlocal audioData
            if self.data.appState == AppState.RECORDING_INPUT:
                audioData.append(inData.copy())

        with sd.InputStream(
            callback=callback,
            samplerate=sampleRate,
            channels=1,
            blocksize=int(sampleRate * blockDuration),
        ):
            while (
                self.data.appState == AppState.RECORDING_INPUT
                and len(audioData) * blockDuration < duration
            ):
                sd.sleep(int(blockDuration * 1000))

        audioData = np.concatenate(audioData, axis=0)
        return audioData, sampleRate


    def playAudio(self):
        pass
