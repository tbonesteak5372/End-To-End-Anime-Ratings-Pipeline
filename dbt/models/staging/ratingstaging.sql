{{ config(materialized='view') }}

SELECT 
    animeid as anime_id,
    userid as user_id,
    rating
FROM {{source('raw','ratings')}}