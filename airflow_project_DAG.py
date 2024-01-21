from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator 
#from airflow.utils.dates import days_ago 
from Dataset import run_etl

default_args ={
    'owner':'airflow',
    'start_date': datetime(2024,7,1),
    'retries':1,
    'retry_delay':timedelta(minutes=1)
}

def greet():
    print("Hello")

with DAG(
    dag_id='project_dag_v2',
    default_args= default_args,
    description = 'Airflow Project DAG',
) as dag:

    running_etl_fun = PythonOperator(
        task_id = 'etl_task_1',
        python_callable=greet,
    )

    running_etl_fun