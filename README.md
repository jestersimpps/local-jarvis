# local-jarvis

This is a setup to have fully offline conversations with local language models.
It should run on any m1 and higher mac. 

I am using faster-whisper for speech to text transcription.
I am using the built in 'say' command on mac for TTS output.

# installation

- Install ollama [https://ollama.com/](https://ollama.com/)
- download any model you would like to use as your llm.
- install your favorite mac os voice and set it in the `config.py`.
- set your custom instructions and the bot's name.
- set your whisper model size [https://github.com/SYSTRAN/faster-whisper](faster-whisper) - small works fine.
- pip install the requirements

# Running

- `python3 main.py`


## Future ideas

- give the bot a memory [https://blog.langchain.dev/langfriend/](https://blog.langchain.dev/langfriend/)
- support online functionality using the `OFFLINE` boolean in the config file.
  - implement [https://groq.com/](groq) as llm api
  - implement elevenlabs as a TTS api [https://elevenlabs.io/ ](elevenlabs)
  - implement async streaming between apis
- maybe implement [https://www.openinterpreter.com/](open interpreter)

## Credits

based on the ideas of [https://github.com/ccappetta](Chris Cappetta) 