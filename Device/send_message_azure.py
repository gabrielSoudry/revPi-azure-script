#!/usr/bin/python3

import random
import time
from azure.iot.device import IoTHubDeviceClient, Message
import os
import datetime

CONNECTION_STRING = os.environ.get("CONNECTION_STRING_DEVICE")

# Define the JSON message to send to IoT Hub.
TEMPERATURE = 20.0
HUMIDITY = 60
MSG_TXT = '{{"temperature": {temperature},"humidity": {humidity},"count": {count}}}'
NBR_MESSAGE = 540
count = 500


def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(
        CONNECTION_STRING)
    return client


def iothub_client_telemetry_sample_run():
    global count
    try:
        client = iothub_client_init()
        print("IoT Hub device sending periodic messages, press Ctrl-C to exit")

        while count < NBR_MESSAGE:
            # Build the message with simulated telemetry values.
            temperature = TEMPERATURE + (random.random() * 15)
            humidity = HUMIDITY + (random.random() * 20)
            msg_txt_formatted = MSG_TXT.format(
                temperature=temperature, humidity=humidity, count=count)
            message = Message(msg_txt_formatted)
            message.content_encoding = "utf-8"
            message.content_type = "application/json"

            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            if temperature > 30:
                message.custom_properties["temperatureAlert"] = "true"
            else:
                message.custom_properties["temperatureAlert"] = "false"

            message.custom_properties["SendingTime"] = datetime.datetime.now()

            # Send the message.
            print("Sending message: {}".format(message))
            client.send_message(message)
            time.sleep(1)
            print("Message successfully sent")
            count += 1

    except KeyboardInterrupt:
        print("IoTHubClient sample stopped")


if __name__ == '__main__':
    print("IoT Hub Quickstart #1 - Simulated device")
    print("Press Ctrl-C to exit")
    iothub_client_telemetry_sample_run()
