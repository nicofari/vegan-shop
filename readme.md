# Vegan shop

## Purpose

Simulates a vegan shop with sell/buy/list operations.

## Requirements
App is written with Python 3.11.
There are no dependencies other than standard library.

## Provisioning
No external services needed, no databases, no queues, nothing.
It's possible to run the application with a standard Python 3.11 container only.
Instructions are provided below.

### Run unit tests

To run unit tests (requires docker):

```
docker run --name test_python --rm -v $(pwd):/app python:3.11-alpine3.17  python -m unittest discover /app
```

### Run locally
To run the application:

```
docker run --name test_python -ti --rm -v $(pwd):/app python:3.11-alpine3.17  python /app/main.py /tmp/vegan_shop_store.json it
```

### Localization support
Application output is multi-lingual.
Supported languages are Italian and English.
Desired country code must be passed as a parameter to the main entrypoint script.

### Data persistency
Shop store data are persisted in json format into a file.
Full file path must be specified as a parameter to the main script.

