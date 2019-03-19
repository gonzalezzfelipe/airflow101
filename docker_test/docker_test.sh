docker-compose \
  -p airflow_101 \
  up \
  --build \
  --force-recreate

docker-compose down
