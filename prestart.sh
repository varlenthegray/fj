#! /usr/bin/env bash

# Set the path for Python (inside venv)
export PYTHONPATH="$PYTHONPATH:$PWD/app"

# Let the DB start
python ./app/backend_pre_start.py

# Generate the migrations file based on our current database model
alembic revision --autogenerate -m "Initial migration"

# Run migrations
alembic upgrade head

# Create initial data in DB
python ./app/initial_data.py