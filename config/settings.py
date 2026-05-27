from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


# Ruta raíz del proyecto (dos niveles arriba: config/ → jarvis/)
BASE_DIR: Path = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):

    # ─── Identidad ─────────────────────────────────
    assistant_name: str = Field(default="Jarvis")
    user_name: str = Field(default="Señor")
    wake_word: str = Field(default="jarvis")

    # ─── LLM ───────────────────────────────────────
    gemini_api_key: str = Field(default="")

    # ─── TTS ───────────────────────────────────────
    tts_voice: str = Field(default="es-PE-AlexNeural")
    tts_rate: str = Field(default="+0%")
    tts_volume: str = Field(default="+0%")

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


# Instancia única (patrón Singleton implícito)
settings = Settings()