
  
    

create or replace transient table DBT_DB.DBT_SCHEMA.intermidatedbt
    
    
    
    as (

SELECT 
r.anime_id, 
a.anime_title,
AVG(r.rating) as average_rating, 
COUNT(r.anime_id) as number_of_ratings
FROM DBT_DB.DBT_SCHEMA.animestaging as a
LEFT JOIN DBT_DB.DBT_SCHEMA.ratingstaging as r 
    ON a.anime_id = r.anime_id
WHERE a.anime_type = 'TV'
GROUP BY r.anime_id, a.anime_title
HAVING COUNT(r.anime_id) > 50
    )
;


  