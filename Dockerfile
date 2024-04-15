FROM python:3.12-bookworm

WORKDIR /app
COPY rinha_de_backend /app
RUN apt-install python3-pip -y && pip install poetry && poetry install

ENTRYPOINT [ "poetry" "shell" "uvicorn" "main:app" ]