


from models import LogLevel


class Config:
  
  
  INSTRUCTIONS = """
  You are Jarvis, a robotic assistant.
  """


  LOCAL_OLLAMA_LLM = "phi3"
  
  LOG_LEVEL = LogLevel.DEBUG
  
  RECORDING_SAMPLE_RATE = 44100
  RECORDING_DURATION = 90  # Seconds
  RECORDING_BLOCK_DURATION = 0.1  # Seconds
