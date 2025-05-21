# DLAI

## Docker Setup Instructions

This repository includes a Docker configuration to run the notebooks in a Jupyter Lab environment.

### Prerequisites

- Docker installed on your system ([Get Docker](https://docs.docker.com/get-docker/))

### Building the Docker Image

To build the Docker image, run the following command from the project root directory:

```bash
docker build -t dlai-jupyter .
```

### Running the Container

To run the container and start Jupyter Lab, use:

```bash
docker run -p 8888:8888 -v $(pwd):/app dlai-jupyter
```

For Windows Command Prompt:
```cmd
docker run -p 8888:8888 -v %cd%:/app dlai-jupyter
```

For Windows PowerShell:
```powershell
docker run -p 8888:8888 -v ${PWD}:/app dlai-jupyter
```

After running the container, you'll see a URL with a token in the console output. Copy and paste this URL into your browser to access Jupyter Lab.

### Stopping the Container

To stop the running container, press `Ctrl+C` in the terminal where the container is running, or find and stop the container using:

```bash
docker ps
docker stop <container_id>
```