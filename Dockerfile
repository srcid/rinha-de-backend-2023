FROM python:3.12-alpine3.19

COPY ./ /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD [ "uvicorn", "rinha_de_backend_2023.main:app", "--host", "0.0.0.0", "--port", "80", "--log-level", "warning" ]

EXPOSE 80