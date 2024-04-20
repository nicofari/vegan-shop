# Vegan shop

## Python exercise

Simulates a vegan shop with sell/buy/list operations.

### Run unit tests via docker

To run unit tests (requires docker):

```
docker run --name test_python --rm -v $(pwd):/app python:3.11-alpine3.17  python -m unittest discover /app
```

To run the application:

```
docker run --name test_python -ti --rm -v $(pwd):/app python:3.11-alpine3.17  python /app/main.py
```

