


from models import LogLevel


class Config:
  
  BOT_NAME = "Vicky"
  INSTRUCTIONS = f"""
  You are {BOT_NAME}, a robotic assistant.
  """

  LOCAL_OLLAMA_LLM = "phi3"
  OFFLINE = True
  
  LOG_LEVEL = LogLevel.INFO
  
  RECORDING_SAMPLE_RATE = 44100
  RECORDING_DURATION = 90  # Seconds
  RECORDING_BLOCK_DURATION = 0.1  # Seconds
  
  WHISPER_MODEL_SIZE = "small"
  WHISPER_DEVICE = "cpu"
  WHISPER_COMPUTE_TYPE = "float32"
