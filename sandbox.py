import subprocess
import sys
import os
import time
import shutil

def create_docker_container(file_path):
    """
    Creates a Docker container, copies the file into the container, 
    and runs it inside the container.
    """
    try:
        # Pull the docker image (ensure to use your custom image or the base Ubuntu image)
        subprocess.run(["docker", "build", "-t", "sandbox-env", "."], check=True)

        # Create the Docker container
        container_name = "sandbox_container"
        subprocess.run(["docker", "create", "--name", container_name, "sandbox-env"], check=True)

        # Copy the file into the container
        file_name = os.path.basename(file_path)
        subprocess.run(["docker", "cp", file_path, f"{container_name}:/app/{file_name}"], check=True)

        # Run the file inside the container (using wine for Windows executables, if necessary)
        subprocess.run(["docker", "start", "-i", container_name, f"wine /app/{file_name}"], check=True)

        # Stop the container after execution
        subprocess.run(["docker", "stop", container_name], check=True)
        subprocess.run(["docker", "rm", container_name], check=True)

        print("File executed successfully in the sandbox.")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while executing the file in Docker: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python sandbox.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)

    create_docker_container(file_path)

if __name__ == "__main__":
    main()
