#!/usr/bin/python3

import threading
import time
from azure.iot.device import IoTHubDeviceClient
import revpimodio
import os

RECEIVED_MESSAGES = 0
CONNECTION_STRING_DEVICE = os.environ.get("CONNECTION_STRING_DEVICE")


def message_listener(client):
    global RECEIVED_MESSAGES
    while True:
        message = client.receive_message()
        RECEIVED_MESSAGES += 1
        print("\nMessage received:")

        myrevpi = revpimodio.RevPiModIO(auto_refresh=True)
        myrevpi.devices.core.A1 = revpimodio.RED
        myrevpi.devices.core.A2 = revpimodio.GREEN

        # This script is not optimized at all and for demo purposes only :)
        for property in vars(message).items():
            if (property[0] == "custom_properties"):
                print(property[1]["testProperty"])
                if (int(property[1]["testProperty"]) == 0):
                    print("ouverure barriere")
                    myrevpi.devices.core.A1 = revpimodio.RED
                    myrevpi.devices.core.A2 = revpimodio.RED
                else:
                    print("fermeture barriere")
                    myrevpi.devices.core.A1 = revpimodio.GREEN
                    myrevpi.devices.core.A2 = revpimodio.GREEN

        print("Total calls received: {}".format(RECEIVED_MESSAGES))
        print()


def iothub_client_sample_run():
    try:
        client = IoTHubDeviceClient.create_from_connection_string(
            CONNECTION_STRING_DEVICE)

        message_listener_thread = threading.Thread(
            target=message_listener, args=(client,))
        message_listener_thread.daemon = True
        message_listener_thread.start()

        while True:
            time.sleep(1000)

    except KeyboardInterrupt:
        print("IoT Hub C2D Messaging device sample stopped")


if __name__ == '__main__':
    print("Starting the Python IoT Hub C2D Messaging device sample...")
    print("Waiting for C2D messages, press Ctrl-C to exit")

    iothub_client_sample_run()
