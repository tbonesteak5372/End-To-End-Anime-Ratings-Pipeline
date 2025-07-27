
# Anime Ratings - End-to-End Data Pipeline

An end-to-end data engineering pipeline demonstrating the use of Apache Airflow, dbt, and Snowflake to extract, load, transform, and visualize anime ratings data from Kaggle. This project simulates a real-world ETL orchestration of 10M records, processed using Python, Docker, and cloud data warehousing.

---

## Project Overview

This pipeline automates the extraction of anime ratings datasets from Kaggle, loads the data into Snowflake using Python's Snowflake connector, transforms the data using dbt, and manages the orchestration using Apache Airflow.

The pipeline is containerized with Docker and structured to support modular development, testing, and scheduling. The entire system is orchestrated in a local environment using Apache Airflow.

---

## Architecture - Anime Ratings Pipeline
<img width="850" height="481" alt="image" src="https://github.com/user-attachments/assets/1c118be9-d878-421a-ac6c-eac45ee5641b" />


---

## Technologies and Functions

| Technology      | Purpose                                 |
|----------------|------------------------------------------|
| Python          | API interaction, data loading to Snowflake |
| Pandas          | Data validation and preprocessing        |
| Snowflake       | Cloud data warehouse (staging & core tables) |
| dbt             | SQL-based data modeling and testing      |
| Apache Airflow  | Task orchestration and scheduling        |
| Docker          | Containerization and environment control |

---

## Project Structure

```
anime_ratings_pipeline/
├── dags/                         # Airflow DAGs
│   └── orchestrate.py
├── data/                         # Raw & cleaned data
├── dbt/                          # dbt project root
│   ├── dbt_project.yml
│   ├── models/
│   │   ├── staging/
│   │   ├── intermediate/
│   │   └── marts/
│   └── profiles/
├── kaggle/                       # Kaggle API credentials
├── docker-compose.yml            # Orchestration config
├── Dockerfile                    # Docker build setup
├── requirements.txt              # Python dependencies
└── images/                       # Project screenshots
    ├── airflow_built.png
    ├── dbt_models_ran.png
    ├── dag_status_success.png
    ├── snowflake_setup.png
    └── system_design.png
```

---

## Entity Relationship Diagram (ERD)
<img width="889" height="575" alt="image" src="https://github.com/user-attachments/assets/508ba7ec-c1cf-470e-bd55-0c426e091042" />

---

## Pipeline Components

### 1. Extract - Kaggle API

- Data is extracted from Kaggle using the `kaggle.api.dataset_download_files()` method.
- Files are saved locally in `.csv` format.
<img width="807" height="132" alt="image" src="https://github.com/user-attachments/assets/a9871b53-287b-456b-b8e2-b2fa0ef40d93" />

---

### 2. Clean & Validate - Python + Pandas

- Cleaned invalid entries (`?` values, nulls).
- Ensured consistent data types and saved validated data to the `data/` folder.
<img width="731" height="186" alt="image" src="https://github.com/user-attachments/assets/79241951-d715-4b38-af05-610800927fff" />

---
## 2.5 Create DW, DB, and Role
<img width="740" height="492" alt="image" src="https://github.com/user-attachments/assets/e2c86005-f89b-4282-981d-8827d5cc2f08" />

### 3. Load to Snowflake - Python Connector

- Used `snowflake-connector-python` to connect to Snowflake.
- Executed `PUT` and `COPY INTO` commands to load cleaned data into **staging tables**.
<img width="1024" height="1270" alt="image" src="https://github.com/user-attachments/assets/c41211b2-9bd1-4809-ab57-1eec252c027d" />

---
### 4. Transform - dbt

- Organized dbt models into three layers:
  - `staging`: Cleans raw data
  - `intermediate`: Combines tables and applies business logic
  - `marts`: Final layer with aggregated and filtered data

- Commands used:
  - `dbt run`
  - `dbt test`
  - `dbt docs generate`
<img width="1547" height="237" alt="dbt modes ran sucessfully" src="https://github.com/user-attachments/assets/8261c7c8-e598-4c2b-8cdc-7c6e459ff7a9" />
---

### 5. Orchestrate - Apache Airflow

- DAG defined in `orchestrate.py` with chained tasks:
  - `get_kaggle_data_from_api`
  - `read_in_csv_for_validation`
  - `run_snowflake_pipeline`
  - `dbt_run`
  - `dbt_test`
  - `dbt_docs`

- Dockerized Airflow runs all steps with a single command.
<img width="1915" height="924" alt="orchestration sucessful" src="https://github.com/user-attachments/assets/7403def3-5145-4546-abf2-65503899f02d" />
---

## Pipeline Runtime Status

- Pipeline successfully runs end-to-end with all tasks marked as complete in Airflow UI.
- Current setup runs on manual trigger but can be scheduled with cron expressions.

---
## Create Role and Allow Apache Preset's IP to connect to SF DB
<img width="717" height="589" alt="image" src="https://github.com/user-attachments/assets/43180b11-6771-49bc-a7c8-a3cf0644364e" />

--

## Dashboard created using Apache Preset:
<img width="1869" height="943" alt="image" src="https://github.com/user-attachments/assets/61be4e67-29fb-4334-8930-e786fd1ab453" />

