from kink import inject
from config import Config
from models import Entity, AppState, LogLevel


@inject
class Data:
    logLevel = LogLevel.INFO
    conversation = []
    appState = AppState.WAITING_FOR_INPUT

    def __init__(self, config: Config):
        self.logLevel = config.LOG_LEVEL

    def setRecordingFinished(self):
        self.isRecordingFinished = True
        if self.logLevel == 0:
            print("Recording finished")

    def clearConversation(self):
        self.conversation = []
        if self.logLevel == 0:
            print("Conversation cleared")

    def addToConversation(self, text: str, entity: Entity):
        self.conversation.append({"role": entity, "content": text})
        if self.logLevel == 0:
            print(f"{entity} added to conversation: {text}")

    def changeAppState(self, state: AppState):
        self.appState = state
        if self.logLevel == 0:
            print(f"App state changed to {state}")
