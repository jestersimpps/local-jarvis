import os
from langchain_community.llms import Ollama
from config import Config

  
# anthropic_key = os.environ("ANTHROPIC_KEY")
# openai_key = os.environ("OPENAI_KEY")


class Llm:

    llm: Ollama
    offline = True

    def __init__(self, config: Config, offline=True):
        if offline:
            self.llm = Ollama(model=config.LOCAL_OLLAMA_LLM)
        else:
            # We will include cloud based LLMs here in the future
            pass
