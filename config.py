from kink import inject
from models import LogLevel

@inject
class Config:
  
  BOT_NAME = "Vicky"
  INSTRUCTIONS = f"""
  You are {BOT_NAME}, a robotic assistant. Try and answer short and concise.
  """
  
  # TTS
  LOCAL_TTS_VOICE="com.apple.speech.synthesis.voice.joelle"
  LOCAL_TTS_RATE=200

  # LLM
  LOCAL_OLLAMA_LLM = "llama3:8b"
  OFFLINE = True
  
  
  # Recording
  RECORDING_SAMPLE_RATE = 44100
  RECORDING_DURATION = 90  # Seconds
  RECORDING_BLOCK_DURATION = 0.1  # Seconds
  
  # Whisper
  WHISPER_MODEL_SIZE = "small"
  WHISPER_DEVICE = "cpu"
  WHISPER_COMPUTE_TYPE = "float32"
  
  LOG_LEVEL = LogLevel.INFO

