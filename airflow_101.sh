# Install Airflow using pip
pip install apache-airflow

# Configuration through environment variables
export AIRFLOW_HOME=$PWD
export AIRFLOW__CORE__LOAD_EXAMPLES=False

airflow initdb
airflow scheduler & \
airflow webserver -p 8080
