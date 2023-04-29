import plotly.io as pio

from custom_plotly_templates.templates.white import CUSTOM_WHITE


def set_template(template: str) -> None:
    """Set the default Plotly template for all future plots.

    Args:
        template: The name of the template to set as the default.
    """
    pio.templates.default = template


__all__ = ["set_template", "CUSTOM_WHITE"]  # noqa: WPS410
