#!/bin/bash
set -e

# Get to the root directory of the repository.
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT" || exit

# Stops the relevant containers.
# Does not destroy the volumes they're on, so the database state persists.
docker-compose -f docker/docker-compose-local.yml stop
