{{ config(materialized='view') }}

SELECT
    animeid AS anime_id,
    title AS anime_title,
    alternative_title,
    type AS anime_type,
    year AS year_released,
    score,
    episodes,
    mal_url,
    sequel,
    image_url,
    genres,
    genres_detailed
FROM {{ source('raw', 'animes') }}
