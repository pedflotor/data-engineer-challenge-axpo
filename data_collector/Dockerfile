FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN pip install fastapi[all] sqlalchemy paho-mqtt

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
