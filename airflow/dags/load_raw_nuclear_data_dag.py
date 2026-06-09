from datetime import datetime

from airflow import DAG
from airflow.hooks.base import BaseHook
from airflow.operators.python import PythonOperator

RAW_DATA_PATH = "/data"
SCRIPTS_PATH = "/opt/airflow/scripts"


def load_raw_nuclear_data() -> list[str]:
    import sys

    sys.path.insert(0, SCRIPTS_PATH)
    from load_raw_data import load_all_csvs

    conn = BaseHook.get_connection("postgres_nuclear")
    return load_all_csvs(RAW_DATA_PATH, db_uri=conn.get_uri())


with DAG(
    dag_id="load_raw_nuclear_data",
    description="Load CSV files from /data into nuclear_source.raw",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["raw", "postgres", "nuclear"],
) as dag:
    load_csvs = PythonOperator(
        task_id="load_csvs_to_postgres",
        python_callable=load_raw_nuclear_data,
    )
