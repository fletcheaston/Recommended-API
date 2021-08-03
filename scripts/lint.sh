#!/bin/bash
set -e

# Get to the root directory of the repository.
ROOT=$(git rev-parse --show-toplevel)
cd "$ROOT"

isort .
black .
mypy . --strict
