# Persisting in powershell

Your PowerShell profile script is a script that runs every time you start a new instance of PowerShell. It's a place where you can store functions, variables, and aliases that you want to use every time you work in PowerShell. The location of your PowerShell profile script can vary depending on the user and the host program. Here's how you can find and access it:

1. **Finding Your Profile Script**:
   - Launch PowerShell.
   - Type the following command and hit Enter:

     ```powershell
     $PROFILE
     ```

    This command will return the path to your current user, current host profile script. This is typically the profile script you would use.

2. **Checking if Your Profile Exists**:
    Before you can edit your profile, you need to check if it exists. In PowerShell, type the following command and hit Enter:

    ```powershell
    Test-Path $PROFILE
    ```

    This command will return `True` if the profile script exists, and `False` if it does not.

3. **Creating Your Profile Script**:
    If the profile script does not exist, you can create it using the following command:

    ```powershell
    New-Item -Path $PROFILE -ItemType File -Force
    ```

    This command will create a new profile script for you.

4. **Editing Your Profile Script**:
    - You can edit your profile script with any text editor you like. For example, to open it in Notepad, you would use the following command:

    ```powershell
    notepad $PROFILE
    ```

    - Alternatively, if you have Visual Studio Code installed, you can use the following command to open your profile script:

    ```powershell
    code $PROFILE
    ```

    In the profile script, you can add the alias you want to have available every time you start PowerShell, such as:

    ```powershell
    New-Alias -Name pip_update -Value "C:\Program Files\Scripts\pip_batch_update.py"
    ```

5. **Reloading Your Profile Script**:
    After you save your changes, you can either restart PowerShell or run the following command to reload your profile script without restarting:

    ```powershell
    . $PROFILE
    ```

Now your PowerShell environment is customized with the aliases or other settings you've added to your profile script, and these will be available every time you open a new PowerShell session.
