#!/bin/bash

# Check if build and twine are installed
if ! command -v build &> /dev/null
then
    echo "build could not be found. Installing build..."
    pip install build
fi

if ! command -v twine &> /dev/null
then
    echo "twine could not be found. Installing twine..."
    pip install twine
fi

# Build the package
echo "Building the package..."
python -m build

# Upload to PyPI
echo "Uploading the package to PyPI..."
twine upload dist/*

echo "Build and upload completed."
