"""
Functions for managing the list of voices from the ElevenLabs API.
"""
import streamlit as st
from utils.logger import logger
from config import DEFAULT_VOICES
from utils.tts import get_voices  

@st.cache_data(ttl=3600)
def get_available_voices():
    """
    Retrieves the list of available voices using safe get_voices().
    Returns the default list if API request fails.

    Returns:
        dict: Dictionary containing {voice_name: voice_id}
    """
    try:
        voices_list = get_voices()  # Safely fetch voices
        voices_dict = {voice["name"]: voice["id"] for voice in voices_list}

        logger.info(f"Successfully fetched {len(voices_dict)} voices from API")
        return voices_dict

    except Exception as e:
        logger.error(f"Failed to fetch voices: {e}")
        logger.info("Using default voices list as fallback")
        return {voice["name"]: voice["id"] for voice in DEFAULT_VOICES}
