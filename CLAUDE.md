# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AsistenteVirtual is a Spanish-language voice assistant built on Google Gemini, with speech-to-text input (via SpeechRecognition + PyAudio), text-to-speech output (via edge-tts), and Google Calendar integration.

## Environment Setup

```bash
# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

API keys and credentials go in `.env` (not committed). Required variables will include `GOOGLE_API_KEY` for Gemini and OAuth credentials for Google Calendar.

## Commands

```bash
# Run the assistant
python main.py

# Format code
black .

# Lint
ruff check .

# Type check
mypy .
```

## Architecture

The project is in early scaffolding. Planned layout:

- `main.py` — entry point, wires together components and starts the assistant loop
- `src/assitant.py` — core assistant logic (note: filename has a typo; keep it for now to avoid breaking git history)
- `config/` — configuration models (pydantic) and settings loading (python-dotenv)
- `utils/` — shared helpers
- `tests/` — test suite

### Key dependencies and their roles

| Package | Role |
|---|---|
| `google-generativeai` | LLM brain (Gemini API) |
| `edge-tts` | TTS output using Microsoft Edge voices |
| `SpeechRecognition` + `PyAudio` | STT input from microphone |
| `google-api-python-client` + auth libs | Google Calendar integration |
| `pydantic` | Config validation with strict typing |
| `loguru` | Logging |
| `python-dotenv` | Loading API keys from `.env` |

Future STT alternatives noted in requirements.txt: `openai-whisper` and `faster-whisper` (local models).
