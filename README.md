
# Sandbox File Execution and Malware Analysis

This project provides a system that allows you to run potentially suspicious files in an isolated Docker container, ensuring that your main system remains unaffected. The system monitors file execution, logs system activity (such as process creation, network connections, and file system changes), and helps detect possible malware behaviors.

## Features
- **File Isolation**: Execute files inside a Docker container, ensuring complete isolation from the host system.
- **Execution Monitoring**: Monitors and logs system events during the file's execution using Sysmon or other monitoring tools.
- **Post-Execution Report**: Generates a detailed report on the file's behavior (e.g., file modifications, process activity, network usage).
- **Secure Environment**: Ensures the file is executed in a controlled and isolated environment, reducing the risk of malware spreading.

## Prerequisites

- **Docker**: This project requires Docker to create isolated containers for file execution.
  - Install Docker from [here](https://docs.docker.com/get-docker/).
  
- **Python 3.x**: The script is written in Python, so you need Python installed on your system.
  - Install Python from [here](https://www.python.org/downloads/).

- **Wine (Optional)**: If you are running Windows executables inside the container, Wine is required for compatibility with Linux-based containers.
  - Install Wine using the following commands:
    - On Ubuntu: `sudo apt install wine`
    - On other distributions, follow the [Wine installation guide](https://wiki.winehq.org/Download).

- **Sysmon**: This tool is used for logging system events such as process creation, network activity, and file system changes inside the container.
  - Sysmon can be installed on the container to capture system events for analysis.

## Installation

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/yourusername/sandbox-file-execution.git
    cd sandbox-file-execution
    ```

2. **Install Python Dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up Docker**:
    - Ensure Docker is installed and running on your machine.
    - On Linux, run: `sudo service docker start`
    - On Windows, launch Docker Desktop.

4. **Set Up Sysmon** (Optional but recommended for detailed logging):
    - Install Sysmon inside your Docker container or use a pre-configured image.
    - You can follow the [Sysmon setup guide](https://github.com/SwiftOnSecurity/sysmon-config) to configure logging.

## Usage

1. **Run the Python Script**:

    To execute a potentially suspicious file in an isolated container and monitor its behavior, run the Python script with the path to the file you want to test.

    ```bash
    python sandbox.py path_to_your_suspicious_file.exe
    ```

2. **File Execution**:
    - The file will be copied to a Docker container.
    - The file will be executed inside the container using Wine (if it's a Windows executable).
    - System events and file activity will be monitored and logged.

3. **Review Results**:
    - After execution, the script will stop the container.
    - You can review the logs and output files to analyze the behavior of the executed file.
    - A report will be generated with information on file system changes, processes, and network connections during the file’s execution.

## Example Output

```plaintext
Creating Docker container for sandbox...
Docker container created.
Copying file into the container...
File copied into the container.
Running file in Docker container...
File executed in the container.
Monitoring container activity...
Stopping the container...
Container stopped.
