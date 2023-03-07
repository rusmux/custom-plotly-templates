from custom_plotly_templates._version import __version__  # noqa: WPS436
from custom_plotly_templates.render_config import RENDER_CONFIG, set_render_config
from custom_plotly_templates.templates import TEMPLATES, WHITE_TEMPLATE, set_template

__all__ = [
    "__version__",
    "set_template",
    "set_render_config",
    "RENDER_CONFIG",
    *TEMPLATES.keys(),
]
