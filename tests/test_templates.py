import plotly.graph_objects as go
import plotly.io as pio
import pytest

from custom_plotly_templates import TEMPLATES, set_template


def test_import_does_not_mutate_default_template() -> None:
    assert pio.templates.default == "plotly"


@pytest.mark.parametrize("template_name", TEMPLATES.keys())
def test_default_template(template_name: str) -> None:
    set_template(template_name)
    assert pio.templates.default == template_name


@pytest.mark.parametrize(["template_name", "template"], TEMPLATES.items())
def test_template(template_name: str, template: go.layout.Template) -> None:
    assert pio.templates[template_name] == template
