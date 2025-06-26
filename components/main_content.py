"""
Main content component for the ElevenLabs TTS application.
"""
import streamlit as st
from io import BytesIO
from utils.voices import get_available_voices
from utils.tts import text_to_speech, generate_preview
from utils.logger import logger
from config import DEFAULT_VOICES

def render_voice_selector():
    """
    Displays a voice selector with a preview feature.

    Returns:
        str: Selected voice ID.
    """
    st.subheader("Select Voice")

    # Get available voices
    voices_dict = get_available_voices()

    # Voice selection layout
    col1, col2 = st.columns([3, 1])

    with col1:
        selected_voice_name = st.selectbox(
            "Select Voice:",
            options=list(voices_dict.keys()),
            index=0,
            help="Choose the voice you want to use"
        )

    selected_voice_id = voices_dict[selected_voice_name]

    # Preview button
    with col2:
        if st.button("🔊 Preview Voice", use_container_width=True):
            with st.spinner("Generating preview..."):
                preview_audio = generate_preview(selected_voice_id)
                if preview_audio:
                    st.session_state.preview_audio = preview_audio

    # Display preview audio if available
    if 'preview_audio' in st.session_state:
        st.audio(st.session_state.preview_audio, format="audio/mp3")

    return selected_voice_id

def render_text_input():
    """
    Displays a text input area and advanced settings.

    Returns:
        tuple: (text input, stability setting, clarity setting).
    """
    st.divider()
    st.subheader("Enter Text")

    # Text input
    text_input = st.text_area(
        "Text to convert into speech:",
        placeholder="Example: Hello, my name is a virtual assistant. I will assist you today.",
        height=150
    )

    # Language detection info
    st.info("💡 The model supports multiple languages and will automatically detect the language used.")

    # Advanced options
    stability = 0.5
    clarity = 0.75

    with st.expander("Advanced Options"):
        stability = st.slider(
            "Voice Stability",
            min_value=0.0,
            max_value=1.0,
            value=stability,
            step=0.1,
            help="Higher values = more consistent voice, lower values = more expressive."
        )

        clarity = st.slider(
            "Clarity",
            min_value=0.0,
            max_value=1.0,
            value=clarity,
            step=0.1,
            help="Higher values enhance clarity and reduce artifacts."
        )

    return text_input, stability, clarity

def render_conversion_section(text_input, voice_id, stability, clarity):
    """
    Displays the conversion section and audio output.

    Args:
        text_input (str): The text to be converted.
        voice_id (str): The selected voice ID.
        stability (float): Voice stability value.
        clarity (float): Voice clarity value.
    """
    # Convert buttons
    col1, col2 = st.columns([1, 1])

    with col1:
        convert_button = st.button("🎤 Convert & Play", use_container_width=True)

    # Process when button is clicked
    if convert_button:
        if text_input:
            with st.spinner("🔄 Converting text to speech..."):
                audio_data = text_to_speech(
                    text_input,
                    voice_id,
                    stability,
                    clarity
                )

                if audio_data:
                    # Create a BytesIO object for the audio data
                    audio_bytes = BytesIO(audio_data)

                    # Display success message with details
                    st.success(f"✅ Successfully converted {len(text_input)} characters into audio.")

                    # Show audio player
                    st.audio(audio_bytes, format="audio/mp3")

                    # Download button
                    with col2:
                        st.download_button(
                            label="💾 Download Audio",
                            data=audio_data,
                            file_name="tts_output.mp3",
                            mime="audio/mp3",
                            use_container_width=True
                        )
                else:
                    st.error("❌ Failed to convert text to speech. Check the logs for details.")
        else:
            st.warning("⚠️ Please enter text first.")

# def render_main_content():
#     """
#     Displays the main content of the application.
#     """
#     try:
#         # Voice selector
#         voice_id = render_voice_selector()

#         # Text input and settings
#         text_input, stability, clarity = render_text_input()

#         # Conversion section
#         render_conversion_section(text_input, voice_id, stability, clarity)

#     except Exception as e:
#         st.error(f"⚠️ An error occurred: {str(e)}")
#         logger.error(f"Application error: {e}")
#         st.info("Check your .env file and ensure the API key is valid and active.")

def render_main_content():
    voices = get_available_voices()

    selected_voice_label = st.selectbox("Select Voice:", list(voices.keys()))
    selected_voice_id = voices[selected_voice_label]

    if st.button("🔊 Preview Voice", type="primary"):
        audio_data = generate_preview(selected_voice_id)
        if audio_data:
            st.audio(audio_data, format="audio/mp3")
        else:
            st.error("Failed to generate preview.")
