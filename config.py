


from models import LogLevel


class Config:
  
  
  INSTRUCTIONS = """
  You are Jarvis, a robotic assistant.
  """


  LOCAL_OLLAMA_LLM = "phi3"
  
  LOG_LEVEL = LogLevel.DEBUG
