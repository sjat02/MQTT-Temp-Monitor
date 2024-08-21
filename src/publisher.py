##Publishing the temperature values

from paho.mqtt import client as mqtt
import random
import time

# Define the callback functions
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

# def on_publish(client, userdata, mid):
#     print(f"Message published with ID: {mid}")

# MQTT Broker settings
broker = "test.mosquitto.org"  # Public MQTT broker for testing
port = 1883  # Default port for MQTT
topic = "sensor/temperature"  # Topic to publish temperature data

# Create an MQTT client instance
client = mqtt.Client()

# Assign the callback functions
client.on_connect = on_connect
# client.on_publish = on_publish

# Connect to the broker
client.connect(broker, port, 60)

# Start the client loop in a separate thread
client.loop_start()

try:
    while True:
        # Generate a random temperature integer between 20 and 30 degrees Celsius
        temperature = random.randint(20, 30)
        # Publish the temperature value to the topic
        result = client.publish(topic, temperature)
        # Check if the message was published successfully
        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print(f"Published temperature value: {temperature}°C")
        else:
            print("Failed to publish message")
        # Wait for 5 seconds before publishing the next value
        time.sleep(2)
except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    # Stop the client loop and disconnect from the broker
    client.loop_stop()
    client.disconnect()



    


