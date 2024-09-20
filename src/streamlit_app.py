
import streamlit as st
import threading
import paho.mqtt.client as mqtt
import time
import pandas as pd
from datetime import datetime

# Shared data store
data = {"sensor/temperature": []}


# Define the topics
topics = ['sensor/temperature']

# Timestamp for tracking when data is received
timestamps = []


# MQTT Callbacks
def on_message(client, userdata, message):
    topic = message.topic
    payload = float(message.payload.decode())  # Convert payload to float
    if topic in data:
        data[topic].append(payload)
        timestamps.append(datetime.now())  # Store the timestamp of the received message


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    for topic in topics:
        client.subscribe(topic)


# MQTT Client Setup
def mqtt_thread():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("test.mosquitto.org", 1883, 60)
    client.loop_forever()


# Start MQTT client in a background thread
mqtt_thread = threading.Thread(target=mqtt_thread)
mqtt_thread.daemon = True
mqtt_thread.start()

# Streamlit App

st.title("MQTT Data Stream")

st.write("### Data from MQTT topic: sensor/temperature")

# Create a placeholder for the chart
chart_placeholder = st.empty()

while True:
    # Check if data is available and lists have the same length
    if len(data["sensor/temperature"]) > 0:
        min_len = min(len(data["sensor/temperature"]), len(timestamps))
        if min_len > 0:
            # Create DataFrame for plotting using only the data up to min_len
            df = pd.DataFrame({
                "Timestamp": timestamps[:min_len],
                "Temperature": data["sensor/temperature"][:min_len]
            })

            # Display the latest values
            st.write(f"Topic: sensor/temperature, Last Value: {data['sensor/temperature'][-1]}")
            
            # Plot the data
            with chart_placeholder.container():
                st.subheader("Temperature vs. Time")
                st.line_chart(df.set_index('Timestamp'))

    time.sleep(1)  # Update every second