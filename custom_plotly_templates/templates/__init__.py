from typing import Dict

import plotly.graph_objects as go
import plotly.io as pio

from custom_plotly_templates.templates.white import WHITE_TEMPLATE


def register_custom_templates() -> Dict[str, go.layout.Template]:
    templates = {}
    for name, item in globals().items():  # noqa: WPS110, WPS421
        if isinstance(item, go.layout.Template):
            pio.templates[name.lower()] = item
            templates[name.lower()] = item
    return templates


def set_template(template: str) -> None:
    """Set the default Plotly template for all future plots.

    Args:
        template: The name of the template to set as the default.
    """
    pio.templates.default = template


TEMPLATES = register_custom_templates()

__all__ = ["set_template", *TEMPLATES.keys()]
