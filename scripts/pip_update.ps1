# Define where the script should be stored.
$DestinationPath = "C:\Program Files\Scripts\pip_batch_update.py"

# Get the directory of the current script
$ScriptDir = Split-Path $MyInvocation.MyCommand.Path

# Copy the Python script to the destination
Copy-Item "$ScriptDir\pip_batch_update.py" $DestinationPath

# Feedback to the user
Write-Host "The pip_batch_update.py script has been copied to $DestinationPath"

# PowerShell does not need to make scripts executable, so we skip the chmod step

# PowerShell does not need to set aliases in the shell configuration file as they can be set directly in the current session
# However, if you want to make the alias persistent across sessions,
# you can add the following line to your PowerShell profile script:
# New-Alias -Name pip_update -Value $DestinationPath

# Set alias in the current session
New-Alias -Name pip_update -Value $DestinationPath

# Feedback to the user
Write-Host "Alias 'pip_update' has been added. Use 'pip_update' to run the script."
