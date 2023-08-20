from get_data import get_geo_data
import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, html, dcc

df = get_geo_data()

fig = go.Figure(
    data=go.Choropleth(
        locations=df["iso_alpha"],
        z=df["price_open"],
        text=df["country"],
        colorscale="Blues",
        autocolorscale=False,
        reversescale=True,
        marker_line_color="darkgray",
        marker_line_width=0.5,
        colorbar_tickprefix="$",
        colorbar_title="Average Price Opening",
    )
)

fig.update_layout(
    title_text="Stock Market by Region",
    geo=dict(showframe=False, showcoastlines=False, projection_type="equirectangular"),
)


app = Dash(__name__)


app.layout = html.Div([html.H1(children="Stock Price Opening"), dcc.Graph(figure=fig)])


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=False)
