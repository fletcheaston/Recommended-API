#!/bin/bash
# If tests fail, the container will exit with an error code.
# We still want teardown to occur, which is why we don't have `set -e` at the top.
# This is also why changing directories into the root directory requires an explicit exit if it fails.

# Get to the root directory of the repository.
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT" || exit

# Run the tests in containers.
docker-compose -f docker/docker-compose-test.yml up --abort-on-container-exit

# Teardown.
docker-compose -f docker/docker-compose-test.yml down --volumes --remove-orphans
docker image rm test-server
