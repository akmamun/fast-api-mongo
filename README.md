## FastAPI Micro Service with Docker, Nginx, and Asynchronous MongoDB (Motor)

###  Installation Instructions

- Create a [virtual environment](https://docs.python.org/3/library/venv.html)
- Install the Python dependencies with
     ```sh
     pip install -r requirements.txt
    ```
- Copy the .env.example file as .env
    ```sh
    cp .env.example .env
    ```
- Ensure that you fill in all the valid environment properties in the .env file.


### Run Locally
- To run the service locally, use the following command:
    ```sh
    uvicorn server:app --reload
    ```


### Run with Docker
- To run the service using Docker, use the following command:
     ```sh
       sudo docker-compose up -d --build
     ```
### Run Docker Compose for Production Build
- Ensure that you have [Docker](https://docs.docker.com/engine/install) and [Docker Compose](https://docs.docker.com/compose/install/) installed

