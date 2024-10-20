# PokeApi

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)

## Introduction
Endpoint to Fetch all berries growth statistics from `pokeapi.co` using FastAPI. FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Features
- High-performance thanks to Starlette and Pydantic.
- Auto-generated interactive API documentation (Swagger UI and ReDoc).
- Dependency injection system.
- Asynchronous request handling.

## Installation

### Prerequisites
- Python 3.10+
- Git

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/dagiraldomu/PokeApi.git
    cd PokeApi
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Environmental Variables

This project requires some environment variables to work correctly. The variables are loaded from a `.env` file. For security reasons, the actual `.env` file is not included in version control.
- Create an `.env` file in the root of the project.
- Copy the contents of `.env-example` to your `.env` file:

   ```bash
   cp .env-example .env
   ```

5. Running tests:
   ```bash
    pytest
    ```

## Usage

### Running the Development Server
To start the development server, run:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
The API will be available at `http://127.0.0.1:8000`.

### Accessing API Documentation
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Deployment
### Using Docker
1. Build the Docker image:
    ```bash
    docker build -t poke-api-image .
    ```

2. Run the Docker container:
    ```bash
    docker run -d --name poke-api-container -p 8000:8000 poke-api-image
    ```

### Deploying to a Cloud Provider
Refer to the specific cloud provider's documentation for deploying FastAPI applications (e.g., AWS, Azure, Google Cloud).
