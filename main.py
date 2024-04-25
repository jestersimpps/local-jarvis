from log import Logging
from config import Config
from llm import Llm
from data import Data
import pygame

Logging.logInfo(f"Instructions: {Config.INSTRUCTIONS}")



# Init the LLM
Llm(Config)


# Init pygame for audio
pygame.mixer.init()
pygame.init()




