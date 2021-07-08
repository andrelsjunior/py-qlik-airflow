from airflow import DAG
from airflow.operators import BashOperator
from airflow.operators import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 7, 6),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
    }


with DAG(dag_id="podcast_dag", schedule_interval="@daily", default_args=default_args) as dag:    
    
    t1 = BashOperator(
        task_id='podcasts',
        bash_command='python /home/airflow/gcs/data/filename.py')      

    t2 = BashOperator(
        task_id='qlik',
        bash_command='python /home/airflow/gcs/data/filename.py')

    t1 >> t2

