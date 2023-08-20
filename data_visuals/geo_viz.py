from get_data import get_geo_data
import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import (
    ThemeChangerAIO,
    template_from_url,
    load_figure_template,
)

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"

df = get_geo_data()

continents = df["region"].unique()


app = Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])

load_figure_template("SOLAR")

header = html.H4("Stock Market Analysis")


checklist = html.Div(
    [
        dbc.Label("Select Continents"),
        dbc.Checklist(
            id="continents",
            options=[{"label": i, "value": i} for i in continents],
            value=continents,
            inline=True,
        ),
    ],
    className="mb-4",
)

side_bar = dbc.Card(
    [
        checklist,
    ],
    body=True,
)

geo_tree_map = dcc.Graph(id="trees")
geo_earth_map = dcc.Graph(id="earth")

app.layout = dbc.Container(
    [
        header,
        dbc.Row(
            [
                dbc.Col(
                    [ThemeChangerAIO(aio_id="theme"), side_bar, geo_earth_map], width=5
                ),
                dbc.Col([geo_tree_map], width=7),
            ]
        ),
    ],
    fluid=True,
    className="dbc",
)


@callback(
    Output("trees", "figure"),
    Output("earth", "figure"),
    Input("continents", "value"),
    Input(ThemeChangerAIO.ids.radio("theme"), "value"),
)
def update_line_chart(continent, theme):
    if continent == []:
        return []

    fig = px.scatter_geo(
        df,
        locations="iso_alpha",
        color="region",
        hover_name="country",
        size="price_open",
        scope="world",
        template=template_from_url(theme),
    )

    figs = px.treemap(
        df,
        path=[px.Constant("world"), "region", "country", "city"],
        values="price_open",
        color="price_open",
        hover_data=["iso_alpha"],
        title="Stock Market Analysis",
        template=template_from_url(theme),
    )

    return figs, fig


if __name__ == "__main__":
    app.run_server(debug=True)
