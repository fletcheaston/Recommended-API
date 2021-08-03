#!/bin/bash

# Used to rebuild the server image.
# Only really required when the libraries get changed or updated.

# Get to the root directory of the repository.
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT" || exit

# Stops the containers if they're running.
# If they're not running, just ignore and continue.
bash ./scripts/stop_containers.sh

# Remove the server container.
docker rm server
docker image rm server

# Same script to rebuild the local containers.
bash ./scripts/setup_containers.sh

# And just stop them for good measure.
bash ./scripts/stop_containers.sh || true
