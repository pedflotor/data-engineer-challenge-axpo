import paho.mqtt.client as mqtt
import json
import time
import threading
import os

MQTT_BROKER = os.getenv("MQTT_BROKER", "mqtt_broker")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "sensors")
OUTPUT_FILE = "/app/storage/raw_data.json"

# Stop execution after 10 seconds
def stop_execution():
    print("Stopping MQTT client...")
    client.loop_stop()
    client.disconnect()

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        print(f"Received: {data}")

        # Append data to the file in persistent storage
        with open(OUTPUT_FILE, "a") as f:
            f.write(json.dumps(data) + "\n")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

# Initialize MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect and start listening
client.connect(MQTT_BROKER, MQTT_PORT, 60)
threading.Timer(10, stop_execution).start()  # Stop after 10 seconds
client.loop_forever()

