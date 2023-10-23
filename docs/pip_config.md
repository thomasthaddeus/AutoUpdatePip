# Cheat Sheets

## **pip Cheat Sheet**

Here's a concise cheat sheet for using `pip`, the package installer for Python:

### **1. Basic Commands**

- **Install a package**:

  ```bash
  pip install package_name
  ```

- **Uninstall a package**:

  ```bash
  pip uninstall package_name
  ```

- **Upgrade pip**:

  ```bash
  pip install --upgrade pip
  ```

- **List installed packages**:

  ```bash
  pip list
  ```

### **2. Package Versions**

- **Install a specific version**:

  ```bash
  pip install package_name==1.0.0
  ```

- **Upgrade a package to its latest version**:

  ```bash
  pip install --upgrade package_name
  ```

- **List outdated packages**:

  ```bash
  pip list --outdated
  ```

### **3. Requirements Files**

- **Generate a requirements file**:

  ```bash
  pip freeze > requirements.txt
  ```

- **Install packages from a requirements file**:

  ```bash
  pip install -r requirements.txt
  ```

### **4. Virtual Environments (using `venv` module)**

- **Create a virtual environment**:

  ```bash
  python -m venv env_name
  ```

- **Activate the virtual environment**:
  - On Windows:

    ```bash
    env_name\Scripts\activate
    ```

  - On macOS and Linux:

    ```bash
    source env_name/bin/activate
    ```

- **Deactivate the virtual environment**:

  ```bash
  deactivate
  ```

### **5. Miscellaneous**

- **Show information about a package**:

  ```bash
  pip show package_name
  ```

- **Search for a package**:

  ```bash
  pip search search_term
  ```

- **Check if packages have compatible dependencies**:

  ```bash
  pip check
  ```

- **Clear pip cache**:

  ```bash
  pip cache purge
  ```

### **6. Using Wheels**

- **Install a package from a `.whl` file**:

  ```bash
  pip install package_name-version.whl
  ```

- **Download (without installing) a package**:

  ```bash
  pip download package_name
  ```

## **pip Config File Cheat Sheet**

Configuring `pip` through a configuration file allows for setting default values for the package installer.
The file names and locations for the `pip` config file vary depending on the operating system.
This cheat sheet will cover how to set up and use a `pip` config file:

### **1. Default Config File Locations**

- **Linux & macOS**:
  - Global: `/etc/pip.conf`
  - User: `~/.pip/pip.conf`

- **Windows**:
  - Global: `C:\ProgramData\pip\pip.ini`
  - User: `C:\Users\<username>\pip\pip.ini`

### **2. Creating & Editing**

- **Use a text editor** to create or edit the above files. For instance, on Linux/macOS:

  ```bash
  nano ~/.pip/pip.conf
  ```

### **3. Common Settings**

- **Set a default package index**:

  ```ini
  [global]
  index-url = https://pypi.myprivate-repo.org/simple
  ```

- **Use both main PyPI and an extra index**:

  ```ini
  [global]
  index-url = https://pypi.org/simple
  extra-index-url = https://pypi.myprivate-repo.org/simple
  ```

- **Set a default proxy**:

  ```ini
  [global]
  proxy = [protocol://][user:password@]proxy.server:port
  ```

- **Disable package cache**:

  ```ini
  [global]
  no-cache-dir = false
  ```

- **Trust a custom package index**:

  ```ini
  [install]
  trusted-host = pypi.myprivate-repo.org
  ```

- **Set default install options**:

  ```ini
  [install]
  install-option =
      --prefix=/desired/prefix/path
  ```

### **4. Environment Variables**

- You can also set environment variables, which will override the config file settings:
  - **Linux & macOS**:

    ```bash
    export PIP_INDEX_URL=https://pypi.myprivate-repo.org/simple
    ```

  - **Windows (cmd.exe)**:

    ```bash
    set PIP_INDEX_URL=https://pypi.myprivate-repo.org/simple
    ```

### **5. Command Line Overrides**

- You can always override both the config file and environment variables using command-line flags:

  ```bash
  pip install --index-url https://pypi.org/simple package_name
  ```

### **6. Viewing Current Configuration**

- To view your current `pip` configuration settings:

  ```bash
  pip config list
  ```

- To edit the configuration using an interactive editor (e.g., nano, vim):

  ```bash
  pip config edit
  ```
