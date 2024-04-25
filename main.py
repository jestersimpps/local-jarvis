from log import Logging
from config import Config
from llm import Llm
from data import Data
import pygame

Logging.logInfo(f"Jarvis instructions: {Config.INSTRUCTIONS}")

class Status:
    WAITING_FOR_INPUT = 1
    RECORDING_INPUT = 2
    PROCESSING_INPUT = 3
    GENERATING_OUTPUT = 4
    PLAYING_OUTPUT = 5


currentState = Status.WAITING_FOR_INPUT

# Init the LLM
Llm(Config)
# Init pygame for audio
pygame.mixer.init()
pygame.init()




