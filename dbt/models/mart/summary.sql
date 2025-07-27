{{ config(materialized='table') }}

SELECT 
    anime_id, 
    anime_title, 
    average_rating, 
    number_of_ratings
FROM {{ref('intermidatedbt')}}
ORDER BY average_rating desc
LIMIT 10