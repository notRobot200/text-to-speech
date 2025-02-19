"""
Sidebar component for the ElevenLabs TTS application.
"""
import streamlit as st

def render_sidebar():
    """
    Displays the sidebar component with application information.
    """
    st.sidebar.header("ℹ️ Information")

    # App information
    st.sidebar.markdown("""
    This application uses the ElevenLabs API to convert text into natural-sounding speech.
    
    **Features:**
    - Text-to-speech conversion
    - Multiple voice options
    - Download audio output
    
    **Usage Tips:**
    - Choose a voice that matches your text type.
    - Use advanced options to adjust output quality.
    - Use the download button to save the result.
    """)

    st.sidebar.divider()