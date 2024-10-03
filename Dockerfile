FROM node:21 AS frontend

WORKDIR /app

COPY wardrobe-frontend/package.json .
COPY wardrobe-frontend/package-lock.json .

RUN npm install

COPY wardrobe-frontend .

RUN npm run build

FROM python:3.11-buster as builder

RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

# The runtime image, used to just run the code provided its virtual environment
FROM python:3.11-slim-buster as runtime

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY wardrobe ./wardrobe

COPY --from=frontend /app/dist ./dist

ENTRYPOINT ["gunicorn", "wardrobe:app", "--bind=0.0.0.0:8080"]
