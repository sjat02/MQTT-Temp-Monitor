#subscribing the published temperature values 

from paho.mqtt import client as mqtt
import time



# Define the callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to the topic
    client.subscribe(topic)

def on_message(client, userdata, message):
    # Decode the message payload and print it
    temperature = message.payload.decode()
    print(f"Received temperature value: {temperature}°C")

# MQTT Broker settings
broker = "test.mosquitto.org"  # Public MQTT broker for testing
port = 1883  # Default port for MQTT
topic = "sensor/temperature"  # Topic to subscribe to

# Create an MQTT client instance
client = mqtt.Client()

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker, port, 60)

# Start the client loop in a separate thread
client.loop_start()

try:
    # Keep the script running to listen for messages
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    # Stop the client loop and disconnect from the broker
    client.loop_stop()
    client.disconnect()


#am i in prague branch