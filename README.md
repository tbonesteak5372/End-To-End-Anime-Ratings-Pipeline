End-to-End Data Pipeline with Airflow, dbt, and Snowflake

Overview

This project demonstrates a complete data engineering pipeline built using:

- **Apache Airflow** for orchestration
- **dbt** for data transformation and testing
- **Snowflake** as the cloud data warehouse
- **Kaggle API** as the data source
- **Docker** for containerization

---

 Project Structure

```
AIRFLOW_PROJECT/
├── dags/                  # Airflow DAGs
├── data/                  # Local data files
├── dbt/                   # dbt project root
│   ├── dbt_project.yml
│   ├── models/
│   └── profiles/
├── kaggle/                # Kaggle API credentials
├── docker-compose.yml     # Orchestration config
├── Dockerfile             # Container definition
└── requirements.txt       # Python dependencies
```

---
Pipeline Steps

Get Data from Kaggle
- Used Kaggle API to download datasets programmatically via Airflow's `PythonOperator`.

Clean & Validate
- Used pandas to clean invalid fields (e.g., convert `'?'` to `NaN`).
- Saved cleaned files to `data/`.

Load to Snowflake
- Used `snowflake-connector-python` to `PUT` and `COPY INTO` cleaned data.
- Created staging tables and schemas.

Transform with dbt
- Organized models into:
  - `staging/`
  - `intermediate/`
  - `marts/`
- Used `dbt run`, `dbt test`, and `dbt docs generate`.

Orchestrate with Airflow
- Defined DAG in `orchestrate.py`
- Chained tasks:
  - `get_kaggle_data_from_api`
  - `read_in_csv_for_validation`
  - `run_snowflake_pipeline`
  - `dbt_run`
  - `dbt_test`
  - `dbt_docs`

---

Running the Pipeline

```bash
# Start Airflow environment
docker compose up --build

# Access Airflow at http://localhost:8080
# Trigger the DAG named 'orchestrate'
```

---

Final Outcome

A reliable, testable pipeline that loads and transforms real data from Kaggle into Snowflake, with full lineage, test coverage, and orchestration.

