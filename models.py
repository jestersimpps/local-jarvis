
class Entity:
    USER = 1
    LLM = 2


class AppState:
    WAITING_FOR_INPUT = 1
    RECORDING_INPUT = 2
    PROCESSING_INPUT = 3
    GENERATING_OUTPUT = 4
    PLAYING_OUTPUT = 5
    
class LogLevel:
    DEBUG = 0
    INFO = 1
