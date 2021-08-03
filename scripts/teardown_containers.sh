#!/bin/bash
set -e

# Get to the root directory of the repository.
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT" || exit

# Start the services.
docker-compose -f docker/docker-compose-local.yml down --volumes --remove-orphans
