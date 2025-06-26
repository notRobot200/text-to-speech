"""
Functions for converting text to speech.
"""
from elevenlabs.client import ElevenLabs
from config import TTS_MODEL, ELEVEN_API_KEY
from utils.logger import logger

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

        # Voice settings
        voice_settings = {
            "stability": stability,
            "similarity_boost": clarity
        }

        # Convert text to speech
        audio_generator = client.text_to_speech.convert(
            voice_id=voice_id,
            text=text,
            model_id=TTS_MODEL,
            voice_settings=voice_settings
        )

        # Combine audio data from generator
        audio_data = b"".join(audio_generator)
        logger.info(f"Successfully converted {len(text)} characters to {len(audio_data)} bytes of audio")
        return audio_data

    except Exception as e:
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
    return text_to_speech(preview_text, voice_id)
