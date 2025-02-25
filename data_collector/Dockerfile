FROM python:3.10-alpine

WORKDIR /app

COPY main.py .  
RUN pip install paho-mqtt  

CMD ["python", "main.py"]
