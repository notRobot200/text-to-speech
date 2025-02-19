"""
Main file of the ElevenLabs Text-to-Speech application.
"""
import streamlit as st
import os
from config import APP_TITLE, APP_DESCRIPTION, APP_ICON, ELEVEN_API_KEY
from components.sidebar import render_sidebar
from components.main_content import render_main_content
from utils.logger import logger

def main():
    """
    Main function of the Streamlit application.
    """
    # Page config
    st.set_page_config(
        page_title=APP_TITLE.replace("🗣️ ", ""),
        page_icon=APP_ICON
    )

    # App title and description
    st.title(APP_TITLE)
    st.markdown(APP_DESCRIPTION)

    try:
        # Check if API key is configured
        if not ELEVEN_API_KEY:
            st.error("⚠️ API key not found. Make sure the .env file contains a valid ELEVEN_API_KEY.")
            st.info("""
            To configure the API key:
            1. Create a `.env` file in the application directory.
            2. Add the following line: `ELEVEN_API_KEY=your_api_key_here`
            3. Restart the application.
            """)
            return

        # Render sidebar
        render_sidebar()

        # Render main content
        render_main_content()

    except Exception as e:
        st.error("An error occurred in the application. Please try again.")
        logger.error(f"Unhandled application error: {e}")

if __name__ == "__main__":
    logger.info("Starting ElevenLabs TTS application")
    main()