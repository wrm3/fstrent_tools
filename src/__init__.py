"""
fstrent_tools - A comprehensive collection of Python utility functions.
"""

__version__ = "0.3.6"

# Import specific functions you want to expose at package level
from .tools_json import load_json, save_json
from .tools_time import get_timestamp
# ... import other specific functions you want to expose

# Define __all__ to specify which names should be exported
__all__ = [
    'load_json',
    'save_json',
    'get_timestamp',
    # ... add other function names you want to expose
]

# You can keep the rest of your existing imports for internal use
from . import (
    tools_convert,
    tools_debug,
    # ... rest of your module imports
)
