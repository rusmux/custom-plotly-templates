__submodules__ = [
        "templates",
        "configs",
]

from .configs import custom_show_config, set_custom_show_config
from .templates import custom_white, set_custom_template
from ._version import __version__

__all__ = ["__version__",
           "custom_white", "set_custom_template",
           "custom_show_config", "set_custom_show_config"]
