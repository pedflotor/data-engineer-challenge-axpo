import json
import time
import paho.mqtt.client as mqtt
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Database setup
DATABASE_URL = "sqlite:///iot_data.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Define IoT Data Model
class SensorData(Base):
    __tablename__ = "sensor_data"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    sensor_id = Column(String, index=True)
    value = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

# MQTT Setup
MQTT_BROKER = "mqtt_broker"
MQTT_PORT = 1883
MQTT_TOPIC = "sensors"

def on_message(client, userdata, message):
    """Process received MQTT messages."""
    session = SessionLocal()
    try:
        payload = json.loads(message.payload.decode("utf-8"))
        sensor_data = SensorData(
            sensor_id=payload.get("sensor_id"),
            value=payload.get("value"),
            timestamp=datetime.utcnow()
        )
        session.add(sensor_data)
        session.commit()
        print(f"Stored: {sensor_data.sensor_id} - {sensor_data.value}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()

client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT)
client.subscribe(MQTT_TOPIC)
client.loop_start()

# # Uncomment to limit the data generation
# # Run for 10 seconds, then stop
# time.sleep(10)
# client.loop_stop()
# client.disconnect()

