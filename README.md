
# Anime Ratings - End-to-End Data Pipeline

An end-to-end data engineering pipeline demonstrating the use of Apache Airflow, dbt, and Snowflake to extract, load, transform, and visualize anime ratings data from Kaggle. This project simulates a real-world ETL orchestration process using Python, Docker, and cloud data warehousing.

---

## Project Overview

This pipeline automates the extraction of anime ratings datasets from Kaggle, loads the data into Snowflake using Python's Snowflake connector, transforms the data using dbt, and manages the orchestration using Apache Airflow.

The pipeline is containerized with Docker and structured to support modular development, testing, and scheduling. The entire system is orchestrated in a local environment using Apache Airflow.

---

## Architecture - Anime Ratings Pipeline

![System Design](./images/system_design.png)

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

This simplified ERD helps map the relationship between anime and ratings datasets, and guides transformations in dbt.

---

## Pipeline Components

### 1. Extract - Kaggle API

- Data is extracted from Kaggle using the `kaggle.api.dataset_download_files()` method.
- Files are saved locally in `.csv` format.

**Screenshot:**
![Kaggle Extraction](./images/dag_status_success.png)

---

### 2. Clean & Validate - Python + Pandas

- Cleaned invalid entries (`?` values, nulls).
- Ensured consistent data types and saved validated data to the `data/` folder.

---

### 3. Load to Snowflake - Python Connector

- Used `snowflake-connector-python` to connect to Snowflake.
- Executed `PUT` and `COPY INTO` commands to load cleaned data into **staging tables**.

**Screenshot:**
![Snowflake Setup](./images/snowflake_setup.png)

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

**Screenshot:**
![dbt Models Ran](./images/dbt_models_ran.png)

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

**Screenshot:**
![Airflow Built](./images/airflow_built.png)

---

## Pipeline Runtime Status

- Pipeline successfully runs end-to-end with all tasks marked as complete in Airflow UI.
- Current setup runs on manual trigger but can be scheduled with cron expressions.

---

## BI Dashboard (Optional)

- Final `marts` tables can be connected to a BI tool like Tableau, Power BI, or Apache Superset for visualization.

---

## How to Run

1. Clone the repo
2. Add your Kaggle JSON to `/kaggle/kaggle.json`
3. Run the pipeline:

```bash
docker compose up --build
```

Airflow UI will be available at: `http://localhost:8080`

