# Airflow_matrics_API

pull the docker image


then run:


docker run -it -p 8080:8080  --env "_AIRFLOW_DB_MIGRATE=true" --env "_AIRFLOW_WWW_USER_CREATE=true" --env "_AIRFLOW_WWW_USER_PASSWORD=admin" apache/airflow:latest webserver

http://localhost:8080
