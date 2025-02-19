"""
Logging configuration for the application.
"""
import logging

def setup_logger():
    """
    Configures and returns a pre-configured logger.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger("elevenlabs_tts_app")
    return logger

# Initialize the logger for use throughout the application
logger = setup_logger()