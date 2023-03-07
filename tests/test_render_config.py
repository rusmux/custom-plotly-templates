import plotly.io as pio

from custom_plotly_templates import RENDER_CONFIG, set_render_config


def test_import_does_not_mutate_default_render_config() -> None:  # noqa: WPS118
    assert not pio.renderers["notebook"].config


def test_default_render_config() -> None:
    set_render_config()
    assert pio.renderers["notebook"].config == RENDER_CONFIG
