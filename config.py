"""
Configuration and constants for the ElevenLabs TTS application.
"""
import streamlit as st

# Ambil API key dari Streamlit secrets
ELEVEN_API_KEY = st.secrets.get("ELEVEN_API_KEY")

if not ELEVEN_API_KEY:
    raise ValueError("ELEVEN_API_KEY tidak ditemukan di Streamlit secrets.")

# Default voices list
# DEFAULT_VOICES = {
#     "Rachel (Default)": "21m00Tcm4TlvDq8ikWAM",
#     "Adam (Masculine American)": "pNInz6obpgDQGcFmaJgB",
#     "Antoni (Masculine British)": "ErXwobaYiN019PkySvjV",
#     "Bella (Soft Feminine)": "EXAVITQu4vr4xnSDxMaL",
#     "Domi (Androgynous)": "AZnzlk1XvdvUeBnXmlld",
#     "Elli (Feminine American)": "MF3mGyEYCl7XYWbV9V6O",
#     "Josh (Energetic Masculine)": "TxGEqnHWrfWFTfGW9XjX",
#     "Sam (Professional Masculine)": "yoZ06aMxZJJ28mfd3POQ",
#     "Arnold (Unique Masculine)": "VR6AewLTigWG4xSOukaG",
#     "Grace (Calm Feminine)": "oWAxZDx7w5VEj9dCyTzz",
#     "Clyde (Strong Masculine)": "2EiwWnXFnvU5JabPnv8n"
# }
DEFAULT_VOICES = {
    "Rachel (Default)": "21m00Tcm4TlvDq8ikWAM",
    "Adam": "pNInz6obpgDQGcFmaJgB",
    "Bella": "EXAVITQu4vr4xnSDxMaL",
    "Josh": "TxGEqnHWrfWFTfGW9XjX"
}


# TTS Model settings
# TTS_MODEL = "eleven_multilingual_v2"
TTS_MODEL = "eleven_turbo_v2_5"

# App settings
APP_TITLE = "🗣️ Text-to-Speech with ElevenLabs"
APP_DESCRIPTION = "Convert text into natural speech using the ElevenLabs API"
APP_ICON = "🎙️"
