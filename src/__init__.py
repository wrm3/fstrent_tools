"""
fstrent_tools - A comprehensive collection of Python utility functions.
"""

__version__ = "0.3.9"

# Import all functions from each module
from .tools_convert import *
from .tools_debug import *
from .tools_decorators import *
from .tools_dicts import *
from .tools_errors import *
from .tools_eval import *
from .tools_files import *
from .tools_formatting import *
from .tools_hyperlinks import *
from .tools_json import *
from .tools_logging import *
from .tools_object import *
from .tools_print import *
from .tools_python import *
from .tools_settings import *
from .tools_sounds import *
from .tools_speak import *
from .tools_strings import *
from .tools_terminal import *
from .tools_time import *
from .tools_video import *
from .tools_voice import *

# Define __all__ to specify which names should be exported
__all__ = (
    tools_convert.__all__ +
    tools_debug.__all__ +
    tools_decorators.__all__ +
    tools_dicts.__all__ +
    tools_errors.__all__ +
    tools_eval.__all__ +
    tools_files.__all__ +
    tools_formatting.__all__ +
    tools_hyperlinks.__all__ +
    tools_json.__all__ +
    tools_logging.__all__ +
    tools_object.__all__ +
    tools_print.__all__ +
    tools_python.__all__ +
    tools_settings.__all__ +
    tools_sounds.__all__ +
    tools_speak.__all__ +
    tools_strings.__all__ +
    tools_terminal.__all__ +
    tools_time.__all__ +
    tools_video.__all__ +
    tools_voice.__all__
)

# Keep the module imports for internal use
from . import tools_convert, tools_debug
