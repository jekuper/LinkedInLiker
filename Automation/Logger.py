import time
import logging
from colorlog import ColoredFormatter
import traceback

# Global variable to control pausing behavior
STEP_PAUSE = False

def set_step_pause(value):
    """Set the global STEP_PAUSE variable."""
    global STEP_PAUSE
    STEP_PAUSE = value

def get_logger():
    """Returns a configured logger."""
    logger = logging.getLogger("custom_logger")
    if not logger.hasHandlers():  # Prevent duplicate handlers
        logger.setLevel(logging.DEBUG)

        # Create a stream handler
        stream_handler = logging.StreamHandler()

        # Define a formatter with colors
        formatter = ColoredFormatter(
            "%(log_color)s%(levelname)s - %(message)s",
            log_colors={
                'DEBUG': 'white',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            },
        )
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
    
    return logger

def log_info(step_description, sleep_duration=1):
    """Log an informational message and optionally pause for confirmation."""
    logger = get_logger()
    if STEP_PAUSE:
        input(f"Step: {step_description}\nPress Enter to continue...")
    else:
        logger.info(step_description)
        time.sleep(sleep_duration)

def log_warning(step_description, sleep_duration=1):
    """Log a warning message and optionally pause for confirmation."""
    logger = get_logger()
    if STEP_PAUSE:
        input(f"Step: {step_description}\nPress Enter to continue...")
    else:
        logger.warning(step_description)
        time.sleep(sleep_duration)

def log_error(step_description, sleep_duration=1):
    """Log an error message with stack trace and optionally pause for confirmation."""
    logger = get_logger()
    try:
        # Log the error with a stack trace
        raise Exception(step_description)
    except Exception as e:
        logger.error(f"An error occurred: {step_description}\n{traceback.format_exc()}")
        if STEP_PAUSE:
            input("Press Enter to continue...")
    time.sleep(sleep_duration)

# Example Usage
if __name__ == "__main__":
    set_step_pause(True)  # Set global pause behavior
    log_info("This is an informational step.")
    set_step_pause(False)  # Disable pause behavior
    log_warning("This is a warning step.")
    log_error("This is an error step.")
