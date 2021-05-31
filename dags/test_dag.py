from datetime import timedelta
from datetime import datetime
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from airflow.operators.hive_operator import HiveOperator
from airflow.utils.dates import days_ago

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 1, 31, 9, 20),
    'end_date': datetime(2020, 11, 15, 9, 20),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 4,
    'concurrency': 5,
    'retry_delay': timedelta(hours=1),
}

hql = "SELECT * FROM company;"
dag = DAG('1ofd_etl', default_args=default_args, description='Daily loading 1ofd data',
          schedule_interval='0 4 * * *')

# t1, t2 and t3 are examples of tasks created by instantiating operators
t0 = BashOperator(task_id='cut_files', bash_command='ps aux | grep airflow', dag=dag)
t0
