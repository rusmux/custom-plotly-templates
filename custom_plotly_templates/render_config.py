"""Custom render configuration for Plotly."""

import plotly.io as pio

RENDER_CONFIG = dict(
    displaylogo=False,
    scrollZoom=True,
    showTips=False,
    toImageButtonOptions=dict(
        format="png",
        scale=5,
    ),
)


def set_render_config() -> None:
    pio.renderers["notebook"].config.update(RENDER_CONFIG)
