import plotly.graph_objects as go
import plotly.io as pio
import pytest

from custom_plotly_templates import set_template
from custom_plotly_templates.templates import CUSTOM_WHITE


def test_import_does_not_mutate_default_template() -> None:
    assert pio.templates.default == "plotly"


@pytest.mark.parametrize("template_name", ["custom_white"])
def test_default_template(template_name: str) -> None:
    set_template(template_name)
    assert pio.templates.default == template_name


@pytest.mark.parametrize(
    ["template_name", "template"],
    [
        ("custom_white", CUSTOM_WHITE),
    ],
)
def test_template(template_name: str, template: go.layout.Template) -> None:
    assert pio.templates[template_name] == template
