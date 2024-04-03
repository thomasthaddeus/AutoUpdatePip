"""utils/get_pip_cmds.py
This script provides utilities for fetching pip command listings and obtaining
help documentation for each command.

Utilizes the subprocess module to execute pip commands and parse the output to
provide a listing of all pip commands, along with their corresponding help
documentation. The help texts are saved to a file for future reference.

Returns:
    None: This script does not return any values but writes data to a file.
"""

import subprocess


def get_pip_commands():
    """
    Retrieves a list of available pip commands.

    Executes the pip command with no arguments to fetch the list of available
    commands, and parses the result to extract the command names.

    Returns:
        list: A list of strings, each representing a pip command.
    """
    # Get the output of `pip` (with no arguments)
    result = subprocess.run(["pip"], capture_output=True, check=True, text=True)
    # Extract the lines after "Commands:"
    lines = result.stdout.split("Commands:\n")[1].splitlines()
    # Extract command names from lines
    commands = [line.split()[0].strip() for line in lines if line]
    return commands


def get_pip_help_for_command(command):
    """
    Fetches the help text for a specified pip command.

    Executes the pip command with the specified command and '--help' argument
    to fetch the help text for the command.

    Args:
        command (str): The name of the pip command for which to fetch the help
        text.

    Returns:
        str: The help text for the specified pip command.
    """
    result = subprocess.run(
        ["pip", command, "--help"], check=True, capture_output=True, text=True
    )
    return result.stdout


def get_help():
    """
    Fetches help texts for all pip commands and saves them to a file.

    Iterates over all available pip commands, fetches their help texts, and
    saves the collected help texts to a file named 'pip_commands_help.txt'.
    """
    all_pip_help_texts = []

    for command in get_pip_commands():
        help_text = get_pip_help_for_command(command)
        all_pip_help_texts.append(help_text)

    # Saving all the help texts to a file
    with open("../data/pip_help_commands.txt", mode="w", encoding="utf-8") as f:
        f.write(
            "\n\n========================================\n\n".join(all_pip_help_texts)
        )
