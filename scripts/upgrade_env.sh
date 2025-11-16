#!/usr/bin/env bash

set -e  # Exit on error

# Update the lockfile with latest allowed dependency versions
uv lock --upgrade

# Sync the environment: install updated dependencies
uv sync

echo "UV dependencies updated and installed."