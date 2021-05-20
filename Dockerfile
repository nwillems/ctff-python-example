FROM python:3.9 as build

ENV POETRY_VERSION=1.1.4
ENV PYTHONUNBUFFERED=1

RUN pip install "poetry==$POETRY_VERSION" && poetry --version

WORKDIR /app
COPY ./poetry.lock ./pyproject.toml /app/

RUN poetry install --no-interaction --no-ansi --no-root

COPY ./ /app

RUN poetry build --format sdist

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
ENV POETRY_VERSION=1.1.4
ENV PYTHONPATH=/app/src
ENV APP_MODULE=app.main:app

WORKDIR /app
COPY --from=build /app/dist/ctff-python-example*.tar.gz /tmp/

RUN pip install "poetry==$POETRY_VERSION" && \
  tar zxvf /tmp/ctff-python-example*.tar.gz --strip 1 && \
  poetry install --no-root
