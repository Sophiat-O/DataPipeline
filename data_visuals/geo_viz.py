import pycountry
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from db_conn import get_engine
from dash import Dash, html, dcc

db_conn = get_engine()

df_company = pd.read_sql("select * from dw_db.stock", con=db_conn)

df_geo = (
    df_company.groupby(["country_code_iso", "country", "price_close_year"])
    .agg({"price_open": "mean"})
    .reset_index()
)


def get_iso_alpha(country):
    if type(country) != None:
        country = pycountry.countries.get(alpha_2=country)
        iso_alpha = country.alpha_3

    return iso_alpha


df_geo["iso_alpha"] = df_geo["country_code_iso"].apply(lambda x: get_iso_alpha(x))

fig = go.Figure(
    data=go.Choropleth(
        locations=df_geo["iso_alpha"],
        z=df_geo["price_open"],
        text=df_geo["country"],
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
