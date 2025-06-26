"""
Configuration and constants for the ElevenLabs TTS application.
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# # API Configuration
# ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")
# if not ELEVEN_API_KEY:
#     raise ValueError("ELEVEN_API_KEY not found. Ensure the variable is available in the .env file.")

ELEVEN_API_KEY = "sk_395b778df80df32b68fe5ab46d6254187ee77197aca61544"

# Default voices list
DEFAULT_VOICES = {
    "Rachel (Default)": "21m00Tcm4TlvDq8ikWAM",
    "Adam (Masculine American)": "pNInz6obpgDQGcFmaJgB",
    "Antoni (Masculine British)": "ErXwobaYiN019PkySvjV",
    "Bella (Soft Feminine)": "EXAVITQu4vr4xnSDxMaL",
    "Domi (Androgynous)": "AZnzlk1XvdvUeBnXmlld",
    "Elli (Feminine American)": "MF3mGyEYCl7XYWbV9V6O",
    "Josh (Energetic Masculine)": "TxGEqnHWrfWFTfGW9XjX",
    "Sam (Professional Masculine)": "yoZ06aMxZJJ28mfd3POQ",
    "Arnold (Unique Masculine)": "VR6AewLTigWG4xSOukaG",
    "Grace (Calm Feminine)": "oWAxZDx7w5VEj9dCyTzz",
    "Clyde (Strong Masculine)": "2EiwWnXFnvU5JabPnv8n"
}

# TTS Model settings
TTS_MODEL = "eleven_multilingual_v2"

# App settings
APP_TITLE = "🗣️ Text-to-Speech with ElevenLabs"
APP_DESCRIPTION = "Convert text into natural speech using the ElevenLabs API"
APP_ICON = "🎙️"
