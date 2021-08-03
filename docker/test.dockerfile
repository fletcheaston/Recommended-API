FROM python:3.9-slim

WORKDIR /app

COPY ../requirements.txt .

RUN pip install -r requirements.txt

COPY .. /app

# Coverage will exit with an error code if a test fails, so we prevent that from killing the container.
# Once we're done, we can kill the container.
ENTRYPOINT coverage run --source='.' manage.py test --verbosity 3 || true && coverage report && coverage html; exit 0
