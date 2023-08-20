import pandas as pd
from db_conn import get_engine
from clean_data import get_iso_alpha

db_conn = get_engine()
sql_stmt = "select * from dw_db.stock"


def get_geo_data():
    df_company = pd.read_sql(sql_stmt, con=db_conn)

    df_geo = (
        df_company.groupby(
            [
                "country_code_iso",
                "city",
                "country",
                "minor_region",
                "region",
                "price_close_year",
            ]
        )
        .agg({"price_open": "mean"})
        .reset_index()
    )

    df_geo["iso_alpha"] = df_geo["country_code_iso"].apply(lambda x: get_iso_alpha(x))

    return df_geo
