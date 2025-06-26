"""
Functions for managing the list of voices from the ElevenLabs API.
"""
import streamlit as st
from elevenlabs.client import ElevenLabs
from config import DEFAULT_VOICES, ELEVEN_API_KEY
from utils.logger import logger

@st.cache_data(ttl=3600)
def get_available_voices():
    """
    Retrieves the list of available voices from the ElevenLabs API.
    Returns the default list if the API request fails.

    Returns:
        dict: Dictionary containing {voice_name: voice_id}
    """
    try:
        client = ElevenLabs(api_key=ELEVEN_API_KEY)
        voice_list = client.voices.get_all()
        logger.debug(f"Raw voices: {voice_list}")
        # Fix jika voice ternyata tuple
        voices_dict = {
            f"{v[0]}": v[1] if isinstance(v, tuple) else f"{v.name} ({v.labels.get('accent', 'Standard')})": v.voice_id
            for v in voice_list
        }
        
        # voice_list = client.voices.get_all()
        # voices_dict = {f"{voice.name} ({voice.labels.get('accent', 'Standard')})": voice.voice_id
        #                for voice in voice_list}

        if voices_dict:
            logger.info(f"Successfully fetched {len(voices_dict)} voices from API")
            return voices_dict
        else:
            logger.warning("API returned empty voices list, using default voices")
            return DEFAULT_VOICES
    except Exception as e:
        logger.error(f"Failed to fetch voices: {e}")
        logger.info("Using default voices list as fallback")
        return DEFAULT_VOICES
