class Entity:
    USER = 1
    LLM = 2


class Data:

    conversation = []
    isRecordingFinished = True

    def setRecordingFinished(self):
        self.isRecordingFinished = True

    def getIsRecordingFinished(self):
        return self.isRecordingFinished

    def clearConversation(self):
        self.conversation = []

    def getConversation(self):
        return self.conversation

    def addToConversation(self, text: str, entity: Entity):
        self.conversation.append((text, entity))
