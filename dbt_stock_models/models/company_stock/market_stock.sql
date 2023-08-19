with dwdb_market as (
	select  id_market,
	        full_name,
	        city_code
    from {{source('stock_model', 'stg_market')}}
),
dwdb_index_stock as (
    select  id_market,
            price_close_date,
            extract(week from price_close_date) as price_close_week,
            extract(month from price_close_date) as price_close_month,
            extract(year from price_close_date) as price_close_year,
            {{eur_to_dollars('price_close')}} as price_close,
            {{eur_to_dollars('price_open')}} as price_open ,
            volume as,
            {{eur_to_dollars('price_high')}} as price_high,
            {{eur_to_dollars('price_low')}} as price_low
    from {{source('stock_model', 'stg_index_stock')}}
    where id_index = '.FCHI'
    UNION
    select  
            id_market,
            price_close_date,
            extract(week from price_close_date) as price_close_week,
            extract(month from price_close_date) as price_close_month,
            extract(year from price_close_date) as price_close_year,
            {{gbp_to_dollars('price_close')}} as price_close,
            {{gbp_to_dollars('price_open') }} as price_open,
            volume,
            {{gbp_to_dollars('price_high')}} as price_high,
            {{gbp_to_dollars('price_low')}} as price_low
    from {{source('stock_model', 'stg_index_stock')}}
    where id_index ='.FTSE'
    UNION
    select 
            id_market,
            price_close_date,
            extract(week from price_close_date) as price_close_week,
            extract(month from price_close_date) as price_close_month,
            extract(year from price_close_date) as price_close_year,
            {{yen_to_dollars('price_close')}} as price_close,
            {{yen_to_dollars('price_open') }} as price_open,
            volume,
            {{yen_to_dollars('price_high')}} as price_high,
            {{yen_to_dollars('price_low')}} as price_low
    from {{source('stock_model', 'stg_index_stock')}}
    where id_index ='.N225'
    UNION
    select  id_market,
            price_close_date,
            extract(week from price_close_date) as price_close_week,
            extract(month from price_close_date) as price_close_month,
            extract(year from price_close_date) as price_close_year,
            price_close,
            price_open,
            volume,
            price_high,
            price_low
    from {{source('stock_model', 'stg_index_stock')}}
    where id_index in ('.DJI','.NDX')
), 
dwdb_market_index as (
    select id_index,
            id_market
    from{{source('stock_model', 'stg_market_index')}}
),
dwdb_geo as (select city_code,
	        city,
	        state_province,
	        country,
	        minor_region,
	        region 
    from {{ source('stock_model', 'stg_geography') }}
),
dwdb_comp_stock as (
    select id_market,
           id_company
    from {{ref('stock')}}
)

select full_name,
        city,
        state_province,
        country,
        minor_region,
        region,
        price_close_date,
        price_close_week,
        price_close_month,
        price_close_year,
        price_close,
        price_open,
        volume,
        price_high,
        price_low
from dwdb_market
join dwdb_geo
on dwdb_market.city_code = dwdb_geo.city_code
join dwdb_comp_stock
on dwdb_comp_stock.id_market = dwdb_market.id_market
join dwdb_market_index
on dwdb_market_index.id_market = dwdb_market.id_market
join dwdb_index_stock
on dwdb_index_stock.id_index = dwdb_market_index.id_index
