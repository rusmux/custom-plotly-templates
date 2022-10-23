"""Custom show configurations for Plotly."""

import plotly.io as pio

custom_show_config = dict(
    displaylogo=False,
    scrollZoom=True,
    showTips=False,
    toImageButtonOptions=dict(
        format="png",
        scale=5,
    ),
)


def set_custom_show_config() -> None:
    pio.renderers["notebook"].config.update(custom_show_config)
