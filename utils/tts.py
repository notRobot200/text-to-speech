"""
Functions for converting text to speech using ElevenLabs API.
"""
from elevenlabs.client import ElevenLabs
from config import TTS_MODEL, ELEVEN_API_KEY
from utils.logger import logger

DEFAULT_VOICES = [
    {"id": "21m00Tcm4TlvDq8ikWAM", "name": "Default Voice"}
]

def get_voices():
    """
    Fetch available voices from ElevenLabs API safely.
    Returns a list of dicts with 'id' and 'name'.
    """
    try:
        client = ElevenLabs(api_key=ELEVEN_API_KEY)
        voices_response = client.voices.get_all()
        voices_list = []

        for v in voices_response:
            if isinstance(v, dict):
                voices_list.append({"id": v.get("voice_id"), "name": v.get("name")})
            elif isinstance(v, tuple) and len(v) >= 2:
                voices_list.append({"id": v[0], "name": v[1]})

        if not voices_list:
            raise ValueError("No voices found in API response.")

        return voices_list

    except Exception as e:
        logger.error(f"Failed to fetch voices: {e}")
        logger.info("Using default voices list as fallback")
        return DEFAULT_VOICES


def text_to_speech(text, voice_id, stability=0.5, clarity=0.75):
    """
    Converts text into audio data using the ElevenLabs API.

    Args:
        text (str): The text to be converted into speech.
        voice_id (str): The ID of the voice to be used.
        stability (float): The stability value of the voice (0.0-1.0).
        clarity (float): The clarity value of the voice (0.0-1.0).

    Returns:
        bytes: Audio data in binary format, or None if an error occurs.
    """
    try:
        logger.info("Starting text-to-speech conversion")
        client = ElevenLabs(api_key=ELEVEN_API_KEY)

        voice_settings = {
            "stability": stability,
            "similarity_boost": clarity
        }

        audio_generator = client.text_to_speech.convert(
            voice_id=voice_id,
            text=text,
            model_id=TTS_MODEL,
            voice_settings=voice_settings
        )

        audio_data = b"".join(audio_generator)
        logger.info(f"Successfully converted {len(text)} characters to {len(audio_data)} bytes of audio")
        return audio_data

    except Exception as e:
        error_msg = str(e)
        if "401" in error_msg or "Unauthorized" in error_msg:
            logger.error("TTS conversion failed: Unauthorized (Free Tier blocked). Consider using Paid Plan.")
        else:
            logger.error(f"Error in text-to-speech conversion: {e}")
        return None


def generate_preview(voice_id):
    """
    Generates a preview audio for the selected voice.

    Args:
        voice_id (str): The ID of the voice to be previewed.

    Returns:
        bytes: Preview audio data.
    """
    preview_text = "Hello, this is a sample of my voice. I can read text with natural intonation."
    audio = text_to_speech(preview_text, voice_id)
    if audio is None:
        logger.warning("Failed to generate preview audio.")
    return audio
