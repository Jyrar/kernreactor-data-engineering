#!/bin/bash
set -euo pipefail

pip install --quiet pandas sqlalchemy psycopg2-binary

airflow db migrate

airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com \
  || true

airflow webserver &
exec airflow scheduler
