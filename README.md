# Pip Batch Update Utility

This utility provides a streamlined way to manage and update your pip packages in batches. It also includes scripts to add `pip_update` to the system environment, allowing the user to easily update pip packages from anywhere within the console.

## Directory Structure

```bash
|   .gitignore
|   LICENSE
|   pyproject.toml
|   README.md
|   requirements.txt
|
+---docs
|       pip_config.md
|       powershell_profile.md
|       TODO.md
|
+---out
|       output.txt
|
\---src
    |   main.py
    |   pip_batch_update.py
    |   version.py
    |   __init__.py
    |
    +---data
    |       pip_help_commands.txt
    |
    +---logs
    |       log_0.txt
    |       log_1.txt
    |
    +---scripts
    |       build_and_push.sh
    |       create_structure.sh
    |       pip_update.ps1
    |       pip_update.sh
    |
    \---utils
            get_pip_cmds.py
            log_utils.py
            __init__.py
```

## Installation

1. Ensure you have Python installed on your machine.
2. Clone this repository to your local machine.
3. Navigate to the `scripts` directory.
4. Execute the appropriate script for your system (`pip_update.ps1` for PowerShell or `pip_update.sh` for bash) to add `pip_update` to the system environment.

    ```bash
    # For PowerShell
    ./pip_update.ps1

    # For bash
    ./pip_update.sh
    ```

## Usage

1. Once `pip_update` has been added to the system environment, simply run the following command to update your pip packages in batches:

    ```bash
    pip_update
    ```

2. Additional utility scripts are provided in the `src/utils` directory:
   - `get_pip_cmds.py`: Provides utilities for fetching pip command listings and obtaining help documentation for each command.
   - `log_utils.py`: Contains a `logrotate` function to handle log rotation in the specified `logs` directory.

## Documentation

- [Pip Configuration](docs/pip_config.md)
- [PowerShell Profile Configuration](docs/powershell_profile.md)

## License

Refer to the [LICENSE](LICENSE) file for license rights and limitations.
