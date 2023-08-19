/* My attempt at building a model using dbt */
{{ config(materialized='table') }}

with dwdb_company as (
    select id_company, 
            company_name,
            trbc_activity_code,
            gics_subindustry_code,
            naics_national_industry_code,
            hq_address_citycode
    from {{ source('stock_model', 'stg_company') }}
),
dwdb_geography as(
    select city_code,
	        city,
	        state_province,
	        country,
	        minor_region,
	        region 
    from {{ source('stock_model', 'stg_geography') }}
), 
dwdb_gics_classification as (

    select gics_subindustry_code,
	    gics_subindustry,
	    gics_industry ,
	    gics_industry_group,
	    gics_sector 
    from {{source('stock_model', 'stg_gics_classification')}}
), 
dwdb_naics_classification as (

    select naics_national_industry_code,
	        naics_national_industry,
	        naics_international_industry ,
	        naics_industry_group,
	        naics_subsector,
            naics_sector
    from {{source('stock_model', 'stg_naics_classification')}}
),
dwdb_trbc_classification as (

    select trbc_activity_code,
	        trbc_activity,
	        trbc_industry,
	        trbc_industry_group,
	        trbc_business_sector,
            trbc_econ_sector
    from {{source('stock_model', 'stg_trbc_classification')}}
),
dwdb_company_stock as (
    select id_company, 
            id_market,
            price_close_date,
            extract(week from price_close_date) as price_close_week,
            extract(month from price_close_date) as price_close_month,
            extract(year from price_close_date) as price_close_year,
            {{eur_to_dollars('price_close')}} as price_close,
            {{eur_to_dollars('price_open')}} as price_open ,
            volume,
            {{eur_to_dollars('price_high')}} as price_high,
            {{eur_to_dollars('price_low')}} as price_low
    from {{source('stock_model', 'stg_company_stock')}}
    where id_market in ('Euronext','FWB')
    UNION
    select id_company, 
            id_market,
            price_close_date,
            extract(week from price_close_date) as price_close_week,
            extract(month from price_close_date) as price_close_month,
            extract(year from price_close_date) as price_close_year,
            {{skw_to_dollars('price_close')}} as price_close,
            {{skw_to_dollars('price_open')}} as price_open,
            volume,
            {{skw_to_dollars('price_high')}} as price_high,
            {{skw_to_dollars('price_low') }} as price_low
    from {{source('stock_model', 'stg_company_stock')}}
    where id_market ='KSE'
    UNION
    select id_company, 
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
    from {{source('stock_model', 'stg_company_stock')}}
    where id_market ='LSE'
    UNION
    select id_company, 
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
    from {{source('stock_model', 'stg_company_stock')}}
    where id_market ='TSE'
    UNION
    select id_company, 
            id_market,
            price_close_date,
            extract(week from price_close_date) as price_close_week,
            extract(month from price_close_date) as price_close_month,
            extract(year from price_close_date) as price_close_year,
            {{twn_to_dollars('price_close')}} as price_close,
            {{twn_to_dollars('price_open') }} as price_open,
            volume,
            {{twn_to_dollars('price_high')}} as price_high,
            {{twn_to_dollars('price_low')}} as price_low
    from {{source('stock_model', 'stg_company_stock')}}
    where id_market ='TWSE'
    UNION
    select id_company, 
            id_market,
            price_close_date,
            extract(week from price_close_date) as price_close_week,
            extract(month from price_close_date) as price_close_month,
            extract(year from price_close_date) as price_close_year,
            price_close,
            price_open,
            volume,
            price_high,
            price_low
    from {{source('stock_model', 'stg_company_stock')}}
    where id_market in ('Nasdaq','NYSE')
)

select id_company,
        company_name, 
        city,
	    state_province,
	    country,
	    minor_region,
	    region,
        gics_subindustry,
	    gics_industry ,
	    gics_industry_group,
	    gics_sector,
        naics_national_industry,
        naics_international_industry ,
        naics_industry_group,
        naics_subsector,
        naics_sector,
        trbc_activity,
        trbc_industry,
        trbc_industry_group,
        trbc_business_sector,
        trbc_econ_sector,
        id_market,
        price_close_date,
        price_close_week,
        price_close_month,
        price_close_year,
        price_close,
        price_open,
        volume,
        price_high,
        price_low    
from dwdb_company
join dwdb_geography 
on 
    dwdb_company.hq_address_citycode = dwdb_geography.city_code
join 
    dwdb_gics_classification
on 
    dwdb_gics_classification.gics_subindustry_code = dwdb_company.gics_subindustry_code
join 
    dwdb_naics_classification
on 
    dwdb_naics_classification.naics_national_industry_code = dwdb_company.naics_national_industry_code
join 
    dwdb_trbc_classification
on 
    dwdb_trbc_classification.trbc_activity_code = dwdb_company.trbc_activity_code
join 
    dwdb_company_stock
on dwdb_company_stock.id_company = dwdb_company.id_company


