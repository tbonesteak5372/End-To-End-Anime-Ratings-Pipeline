from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta 
import requests 
from anime_pipeline_dag import get_kaggle_data_from_api, read_in_csv_for_validation, connect_to_snowflake, tble_creation_and_staging

def run_snowflake_pipeline():
    conn = connect_to_snowflake()
    tble_creation_and_staging(conn)

dag = DAG(
    dag_id= 'orchestrate',
    default_args={'start_date': datetime.now() - timedelta(days=1)},
    schedule='@monthly',
     catchup=False
)

kaggle_data_task = PythonOperator(
    task_id='get_kaggle_data_from_api',
    python_callable=get_kaggle_data_from_api,
    dag=dag
)

read_csv_task = PythonOperator(
    task_id='read_in_csv_for_validation',
    python_callable=read_in_csv_for_validation,
    dag=dag
)
run_snowflake_pipeline_task = PythonOperator(
task_id='run_snowflake_pipeline',
python_callable=run_snowflake_pipeline,
dag=dag
)

dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd /opt/airflow/dbt && dbt run'
)

dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd /opt/airflow/dbt && dbt test'
)

dbt_docs = BashOperator(
    task_id='dbt_docs',
    bash_command='cd /opt/airflow/dbt && dbt docs generate',
    dag=dag
)


# dependencies 
kaggle_data_task >> read_csv_task >> run_snowflake_pipeline_task >> dbt_run >> dbt_test >> dbt_docs