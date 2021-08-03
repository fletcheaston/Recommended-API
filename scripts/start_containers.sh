#!/bin/bash
set -e

# Get to the root directory of the repository.
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT" || exit

# Should be run AFTER you've set up your containers.
# Starts the relevant containers.
docker-compose -f docker/docker-compose-local.yml start
