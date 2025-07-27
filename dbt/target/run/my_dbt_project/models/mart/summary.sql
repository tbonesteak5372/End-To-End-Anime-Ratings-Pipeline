
  
    

create or replace transient table DBT_DB.DBT_SCHEMA.summary
    
    
    
    as (

SELECT 
    anime_id, 
    anime_title, 
    average_rating, 
    number_of_ratings
FROM DBT_DB.DBT_SCHEMA.intermidatedbt
ORDER BY average_rating desc
LIMIT 10
    )
;


  