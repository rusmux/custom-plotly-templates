import plotly.graph_objects as go
import plotly.io as pio

CUSTOM_WHITE = pio.templates["plotly_white"]
CUSTOM_WHITE.update(
    dict(
        data=dict(
            histogram=[go.Histogram(histnorm="probability")],
            pie=[go.Pie(textinfo="label+percent", insidetextfont_color="white")],
        ),
        layout=dict(
            font=dict(
                color="black",
                size=14,  # noqa: WPS432
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
            margin=dict(t=100, b=40),  # noqa: WPS432
            dragmode="pan",
            modebar_remove=["autoScale", "lasso2d", "select"],
            modebar_activecolor="#F39C12",
        ),
    )
)
pio.templates["custom_white"] = CUSTOM_WHITE
