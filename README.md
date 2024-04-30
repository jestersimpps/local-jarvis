# Local-Jarvis

[![DEMO](https://img.youtube.com/vi/XKjB0ug3sWk/0.jpg)](https://www.youtube.com/watch?v=XKjB0ug3sWk)


This is a setup to have fully offline conversations with local language models.
It should run on any M1 and higher Mac.
I am using Faster-Whisper for speech-to-text transcription.
I am using the built-in 'say' command on mac for TTS output.

# Installation
- Install Ollama [https://ollama.com/](https://ollama.com/)
- Download any model you would like to use as your LLM
- Install your favorite Mac OS voice and set it in the `config.py`.
- Set your custom instructions and the bot's name.
- Set your Whisper model size [https://github.com/SYSTRAN/faster-whisper](faster-whisper) - small works
fine.
- Pip install the requirements

# Running
- `python3 main.py`


## Future ideas
- Give the bot a memory [https://blog.langchain.dev/langfriend/](https://blog.langchain.dev/langfriend/)
- Support online functionality using the `OFFLINE` boolean in the config file.
   - Implement [Groq](https://groq.com/) as LLM API
   - Implement ElevenLabs as a TTS API [ElevenLabs](https://elevenlabs.io/ )
   - Implement async streaming between APIs

## Credits
- Based on the ideas of [CC Appetta](https://github.com/ccappetta)