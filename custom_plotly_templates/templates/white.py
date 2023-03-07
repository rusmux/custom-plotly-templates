import plotly.graph_objects as go
import plotly.io as pio

WHITE_TEMPLATE = pio.templates["plotly_white"]
WHITE_TEMPLATE.update(
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
