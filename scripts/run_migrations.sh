#!/bin/bash
set -e

# Get to the root directory of the repository.
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

# Start the services.
docker-compose -f docker/docker-compose-local.yml start

# Run the migration command from inside the server container.
CONTAINER_ID=$(docker ps -aqf "name=server")
docker exec -t "$CONTAINER_ID" bash -c "python manage.py migrate"

# Shut down the services.
docker-compose -f docker/docker-compose-local.yml stop
