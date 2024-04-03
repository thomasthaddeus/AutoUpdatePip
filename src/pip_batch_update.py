"""pip_batch_update.py

A script to batch update outdated pip packages.

This script identifies outdated pip packages, updates them in batches of 10,
logs errors, and displays the difference between initially outdated and
post-updated packages.

Returns:
    None: The results are printed to the console and errors are logged.

Yields:
    None: This script does not contain a generator for external consumption.
"""

import os
import sys
import subprocess
import logging
from .utils import logrotate, get_help, get_pip_cmds, get_pip_commands, get_pip_help_for_command


def setup_logging():
    """
    Initialize logging configuration.

    Sets up logging to save error messages to a dedicated file located in
    a hidden directory within the user's home folder.

    Returns:
        None: This function directly initializes the logging configuration.
    """
    log_dir = os.path.expanduser("~/.pip_update_logs")

    # Check if we have write permissions for the parent directory
    if not os.access(os.path.dirname(log_dir), os.W_OK):
        print("You do not have permission to write to the log directory. Exiting.")
        sys.exit(1)

    # Check if directory exists, and if not, create it
    if os.path.exists(log_dir):
        print(f"The directory {log_dir} already exists.")
    else:
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, "error_log.txt")
    if os.path.exists(log_file):
        overwrite = (
            input(f"The log file {log_file} already exists. Overwrite? (y/n): ")
            .strip()
            .lower()
        )
        if overwrite != "y":
            print("Exiting without overwriting the log file.")
            sys.exit(1)

    logging.basicConfig(
        filename=log_file,
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    # Call logrotate function after setting up logging
    logrotate()

def get_outdated_packages():
    """
    Return a list of outdated pip packages.

    Executes the pip list command and parses the output to identify outdated packages.

    Returns:
        list: A list of strings representing the names of outdated pip packages.
    """
    try:
        result = subprocess.run(
            ["pip", "list", "--outdated"],
            capture_output=True,
            text=True,
            check=True
        )
        lines = result.stdout.splitlines()[2:]  # ignore the headers
        return [line.split()[0] for line in lines]
    except subprocess.CalledProcessError:
        logging.error("Error occurred while fetching outdated packages.")
        return []

def update_packages(packages):
    """
    Update the given list of pip packages and log any errors.

    For each package that encounters an error during update, the error is logged
    to the designated log file.

    Args:
        packages (list): A list of package names (strings) to be updated.
    """
    try:
        subprocess.run(["pip", "install", "--upgrade"] + packages, check=True)
    except subprocess.CalledProcessError:
        logging.error(
            "Error occurred while updating packages: %s", ', '.join(packages)
        )

def batcher(iterable, n=1):
    """
    Yield successive n-sized chunks from iterable using recursion.

    This generator function is useful for processing items in batches.

    Args:
        iterable (iterable): The source iterable to be split into chunks.
        n (int, optional): The size of each chunk. Defaults to 1.

    Yields:
        list: Lists of items, each of size n (or smaller if fewer than n items
        remain).
    """
    if not iterable:
        return
    yield iterable[:n]
    yield from batcher(iterable[n:], n)
