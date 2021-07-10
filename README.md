## FastAPI MicroService with Docker, Nginx and MongoDB(Motor)

### Create [virtual environment](https://docs.python.org/3/library/venv.html) and install requirements 
```sh
pip install -r requirements.txt
```

### Run docker compose
- Make sure [docker](https://docs.docker.com/engine/install) and [docker-compose](https://docs.docker.com/compose/install/) installed

### Lets Run
- Docker run `sudo docker-compose up -d --build`
- Locally run  `uvicorn src.servers.start:app --reload`
