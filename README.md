# MQTT-Temp-Monitor

**MQTT-Temp-Monitor** is a simple IoT project that demonstrates the use of MQTT (Message Queuing Telemetry Transport) protocol to publish, subscribe to, and visualize temperature data. The project consists of three main components:

1. **Publisher**: A Python script that simulates a temperature sensor by generating random temperature values. These values are published to an MQTT broker under a specific topic (`sensor/temperature`).

2. **Subscriber**: A Python script that listens to the same MQTT topic and receives the temperature data in real-time. The subscriber then processes and displays the received temperature values.

3. **Streamlit Visualizer**: A Python script that also subscribes to the MQTT topic and visualizes the received temperature data in real-time using a line chart. This script is built using Streamlit, a Python library for creating interactive web apps.

This project is ideal for learning the basics of MQTT, and how it can be used to facilitate communication between IoT devices, along with a simple demonstration of real-time data visualization.

## Project Structure

- `src/`: Contains the source code for the project.
  - `publisher.py`: Publishes random temperature values to the MQTT broker.
  - `subscriber.py`: Subscribes to the MQTT topic and receives temperature values.
  - `streamlit_visualizer.py`: Subscribes to the MQTT topic and visualizes the temperature data in real-time using Streamlit.

## Requirements

- Python 3.x
- Paho MQTT library
- Streamlit
- Pandas

You can install the required libraries using:
```bash
pip install paho-mqtt streamlit pandas
