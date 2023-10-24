#!/bin/bash

# Create the main directories
mkdir -p src/utils scripts docs src/logs

# Create the necessary files
touch LICENSE \
      README.md \
      src/__init__.py \
      src/pip_batch_update.py \
      src/utils/__init__.py \
      src/utils/get_pip_cmds.py \
      src/utils/log_utils.py \
      scripts/pip_update.ps1 \
      scripts/pip_update.sh \
      docs/pip_config.md \
      docs/powershell_profile.md \
      pyproject.toml \
      .gitignore

echo "Directory structure created."
