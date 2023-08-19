
{% macro eur_to_dollars(column_name, scale=2) %}
    ({{ column_name }} * 1.09)::numeric(16, {{ scale }})
{% endmacro %}

{% macro skw_to_dollars(column_name, scale=2) %}
    ({{ column_name }} * 0.0007)::numeric(16, {{ scale }})
{% endmacro %}

{% macro gbp_to_dollars(column_name, scale=2) %}
    ({{ column_name }} * 1.27)::numeric(16, {{ scale }})
{% endmacro %}

{% macro yen_to_dollars(column_name, scale=2) %}
    ({{ column_name }} * 0.0069)::numeric(16, {{ scale }})
{% endmacro %}

{% macro twn_to_dollars(column_name, scale=2) %}
    ({{ column_name }} * 0.031)::numeric(16, {{ scale }})
{% endmacro %}
