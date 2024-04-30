from kink import inject
from langchain_community.llms import Ollama
from audio import Audio
from config import Config
from data import Data
from logging import Logging
from models import Entity


# anthropic_key = os.environ("ANTHROPIC_KEY")
# openai_key = os.environ("OPENAI_KEY")


@inject
class Llm:

    def __init__(self, config: Config, data: Data, logging: Logging, audio: Audio):
        self._config = config
        self._data = data
        self._logging = logging
        self._audio = audio

        if config.OFFLINE:
            self._llm = Ollama(model=config.LOCAL_OLLAMA_LLM)
        else:
            # We will include cloud based LLMs here in the future
            pass

    def processResponse(self, prompt: str) -> str:
        llmResponse = ""
        buffer = ""
        minChunkSIze = 150
        splitters = (".", "?", "!")
        prompt = prompt.strip()

        if prompt:
            self._data.addToConversation(prompt, Entity.USER)
        else:
            self._logging.logInfo("Received empty input, skipping...")
            return

        validatedHistory = [
            msg for msg in self._data.conversation if msg.get("content").strip()
        ]

        try:
            for text in self._llm.stream(validatedHistory):
                self._logging.logLlm(text)
                llmResponse += text
                buffer += text
                # Check if buffer is ready to be chunked
                lastSPlitterPos = max(buffer.rfind(splitter) for splitter in splitters)
                if len(buffer) >= minChunkSIze and lastSPlitterPos != -1:
                    chunk = buffer[: lastSPlitterPos + 1]
                    buffer = buffer[lastSPlitterPos + 1 :]

                    # Queue this chunk for async TTS processing
                    self._audio.addToAsyncTextToSpeechQueue(chunk)
        except Exception as e:
            self._logging.logError(f"Error during LLM response: {e}")
            return

        # Process any remaining text in buffer
        if buffer:
            self._audio.addToAsyncTextToSpeechQueue(buffer)

        # Append full response to the conversation history
        self._data.addToConversation(llmResponse, Entity.LLM)
