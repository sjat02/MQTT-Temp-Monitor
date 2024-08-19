# MQTT-Temp-Monitor

**MQTT-Temp-Monitor** is a simple IoT project that demonstrates the use of MQTT (Message Queuing Telemetry Transport) protocol to publish and subscribe to temperature data. The project consists of two main components:

1. **Publisher**: A Python script that simulates a temperature sensor by generating random temperature values. These values are published to an MQTT broker under a specific topic (`sensor/temperature`).

2. **Subscriber**: A Python script that listens to the same MQTT topic and receives the temperature data in real-time. The subscriber then processes and displays the received temperature values.

This project is ideal for learning the basics of MQTT and how it can be used to facilitate communication between IoT devices. By following the setup instructions, you can easily deploy and run the project locally or on any system that supports Python.

## Project Structure

- `src/`: Contains the source code for the project.
  - `publisher.py`: Publishes random temperature values to the MQTT broker.
  - `subscriber.py`: Subscribes to the MQTT topic and receives temperature values.

## Requirements

- Python 3.x
- Paho MQTT library

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mqtt-temp-monitor.git
   cd mqtt-temp-monitor
