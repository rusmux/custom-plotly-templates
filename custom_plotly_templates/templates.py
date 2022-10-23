"""Custom templates for Plotly."""

import plotly.graph_objects as go
import plotly.io as pio

custom_white = go.layout.Template(
    dict(
        data=dict(
            histogram=[go.Histogram(histnorm="probability")],
            pie=[go.Pie(textinfo="label+percent", insidetextfont_color="white")],
        ),
        layout=dict(
            font=dict(
                color="black",
                size=14,
            ),
            xaxis=dict(
                tickcolor="white",
                ticklen=5,
                ticks="outside",
            ),
            yaxis=dict(
                tickcolor="white",
                ticklen=5,
                ticks="outside",
            ),
            legend=dict(
                itemclick="toggleothers",
                itemdoubleclick="toggle",
            ),
            margin=dict(t=100, b=40),
            dragmode="pan",
            modebar_remove=["autoScale", "lasso2d", "select"],
            modebar_activecolor="#F39C12",
        ),
    )
)

pio.templates["custom_white"] = custom_white


def set_custom_template(template: str) -> None:
    if template == "custom_white":
        pio.templates.default = "plotly_white+custom_white"
    else:
        raise ValueError(f"\"{template}\" is not a valid template. "
                         f"Template must be one of: [\"custom_white\"]")
