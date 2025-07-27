
  create or replace   view DBT_DB.DBT_SCHEMA.ratingstaging
  
  
  
  
  as (
    

SELECT 
    animeid as anime_id,
    userid as user_id,
    rating
FROM DBT_DB.DBT_SCHEMA.ratings
  );

