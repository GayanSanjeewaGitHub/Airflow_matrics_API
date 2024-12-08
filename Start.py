import requests
from requests.auth import HTTPBasicAuth

# Airflow server details
AIRFLOW_BASE_URL = "http://localhost:8080/api/v1"
USERNAME = "admin"  # Your Airflow username
PASSWORD = "admin"  # Your Airflow password

# Function to authenticate and get Airflow metrics
def get_airflow_metrics(endpoint, params=None):
    """
    Fetch metrics from Airflow REST API.

    :param endpoint: API endpoint (e.g., 'dags', 'pools', 'variables').
    :param params: Query parameters for the request.
    :return: Response JSON data or error.
    """
    url = f"{AIRFLOW_BASE_URL}/{endpoint}"
    try:
        response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Airflow: {e}")
        return None

if __name__ == "__main__":
    # Example: Fetch list of DAGs
    print("Fetching DAG metrics...")
    dags_data = get_airflow_metrics("dags")
    if dags_data:
        for dag in dags_data.get("dags", []):
            print(f"DAG ID: {dag['dag_id']}, Is Active: {dag['is_active']}")

    # Example: Fetch task instances for a specific DAG
    print("\nFetching task metrics for DAG 'example_dag_id'...")
    task_data = get_airflow_metrics("dags/example_dag_id/dagRuns")
    if task_data:
        for run in task_data.get("dag_runs", []):
            print(f"DAG Run ID: {run['dag_run_id']}, State: {run['state']}")

    # Example: Fetch
