#!/bin/bash

# Define where the script should be stored.
DESTINATION_PATH="/usr/local/bin/pip_batch_update.py"

# Get the directory of the current script
SCRIPT_DIR="$(dirname "$0")"

# Copy the Python script to the destination
cp "$SCRIPT_DIR/pip_batch_update.py" "$DESTINATION_PATH"

# Make the copied script executable
chmod +x "$DESTINATION_PATH"

# Feedback to the user
echo "The pip_batch_update.py script has been copied to $DESTINATION_PATH"

# Check the user's shell and update the appropriate configuration file
SHELL_CONFIG=""
case $SHELL in
    */bash)
        SHELL_CONFIG="$HOME/.bashrc"
        ;;
    */zsh)
        SHELL_CONFIG="$HOME/.zshrc"
        ;;
    */fish)
        # Fish shell uses a different syntax for aliases.
        echo "alias pip_update='$DESTINATION_PATH'" > "$HOME/.config/fish/config.fish"
        echo "Alias 'pip_update' has been added to Fish config."
        ;;
    *)
        # Unknown shell, user will have to add the alias manually
        echo "Unknown shell detected. You may have to add the alias manually."
        echo "Use the following alias:"
        echo "alias pip_update='$DESTINATION_PATH'"
        exit 1
        ;;
esac

if [[ ! -z "$SHELL_CONFIG" ]]; then
    echo "alias pip_update='$DESTINATION_PATH'" >> "$SHELL_CONFIG"
    echo "Alias 'pip_update' has been added to $SHELL_CONFIG"
    echo "Please restart your terminal or run 'source $SHELL_CONFIG' to use the alias."
fi
