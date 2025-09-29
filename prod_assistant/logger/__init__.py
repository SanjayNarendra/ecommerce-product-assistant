# logger/__init__.py
from .custom_logger import CustomLogger

# single shared logger instance
GLOBAL_LOGGER = CustomLogger().get_logger("prod_assistant")