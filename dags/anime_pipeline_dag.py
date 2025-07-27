from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import snowflake.connector as sf
import os 
from dotenv import load_dotenv 

def get_kaggle_data_from_api(): ## Fetch Anime Data From the Kaggle API
# Set this before calling Kaggle API
    os.environ['KAGGLE_CONFIG_DIR'] = '/opt/airflow/.kaggle'
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('tavuksuzdurum/user-animelist-dataset', path='data/', unzip = True)

def read_in_csv_for_validation():
    anime_df = pd.read_csv('data/animes.csv')
    rating_df = pd.read_csv('data/ratings.csv', nrows=10000000)

    anime_df['year'] = pd.to_numeric(anime_df['year'], errors='coerce').astype('Int64')
    anime_df['score'] = pd.to_numeric(anime_df['score'], errors='coerce')  # fix here

    rating_df.to_csv('data/ratings_clean.csv',index=False)
    anime_df.to_csv('data/animes_clean.csv', index=False)

def connect_to_snowflake():
    # Connect to Snowflake
    load_dotenv()
    conn = sf.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
    )

    return conn 

def tble_creation_and_staging(conn):
    # Load csv to staging tables
    cs = conn.cursor()
    cs.execute("USE ROLE DBT_ROLE")
    cs.execute("USE DATABASE DBT_DB")
    cs.execute("USE SCHEMA DBT_SCHEMA")

    cs.execute("""      
        CREATE TABLE IF NOT EXISTS ANIMES (
            animeID           INTEGER NOT NULL PRIMARY KEY,
            title             VARCHAR(255),
            alternative_title VARCHAR(255),
            type              VARCHAR(100),
            year              INTEGER,
            score             FLOAT,
            episodes          INTEGER,
            mal_url           VARCHAR(500),
            sequel            VARCHAR(255),
            image_url         VARCHAR(500),
            genres            TEXT,
            genres_detailed   TEXT
        );
    """)


    cs.execute("""
            CREATE TABLE IF NOT EXISTS RATINGS (
            userID  INTEGER NOT NULL,
            animeID INTEGER,
            rating  INTEGER
        );
              """)

    cs.execute("CREATE OR REPLACE STAGE DBT_STAGE")

    cs.execute("PUT file://data/animes_clean.csv @DBT_STAGE auto_compress=true")
    cs.execute("PUT file://data/ratings_clean.csv @DBT_STAGE auto_compress=true")

    cs.execute("""
        COPY INTO animes
        FROM @DBT_STAGE/animes_clean.csv.gz
        FILE_FORMAT = (TYPE = CSV SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY = '"');
    """)

    cs.execute("""
        COPY INTO ratings
        FROM @DBT_STAGE/ratings_clean.csv.gz
        FILE_FORMAT = (TYPE = CSV SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY = '"');
    """)

