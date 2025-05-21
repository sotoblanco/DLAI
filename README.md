# DLAI

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/username/DLAI.git
cd DLAI
```

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

After running the container, you'll see a URL with a token in the console output. Copy and paste this URL into your browser to access Jupyter Lab.

### Stopping the Container

To stop the running container, press `Ctrl+C` in the terminal where the container is running, or find and stop the container using:

```bash
docker ps
docker stop <container_id>
```

llm_log/
Contains the logs of the LLMs used to generate the code and the situation for the assignments

lab/
Contains the lab notebooks and the solution notebooks

unittests.py
Contains the unit tests for the code

requirements.txt
Contains the requirements for the project




