from config import Config
from models import Entity, State


class Data:

    def __init__(self, config: Config):
        self.logLevel = config.LOG_LEVEL

    logLevel = 0
    conversation = []
    isRecordingFinished = True
    appState = State.WAITING_FOR_INPUT

    def setRecordingFinished(self):
        self.isRecordingFinished = True
        if self.logLevel == 0:
            print("Recording finished")

    def getIsRecordingFinished(self):
        return self.isRecordingFinished

    def clearConversation(self):
        self.conversation = []
        if self.logLevel == 0:
            print("Conversation cleared")

    def getConversation(self):
        return self.conversation

    def addToConversation(self, text: str, entity: Entity):
        self.conversation.append((text, entity))
        if self.logLevel == 0:
            print(
                f"{'LLM' if entity == Entity.LLM else 'User'} added to conversation: {text}"
            )

    def changeAppState(self, state: State):
        self.appState = state
        if self.logLevel == 0:
            print(f"App state changed to {state}")
