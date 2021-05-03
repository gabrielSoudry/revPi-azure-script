#!/usr/bin/python3

import random
import sys
from azure.iot.hub import IoTHubRegistryManager
from dotenv import load_dotenv
import os 

MESSAGE_COUNT = 2
AVG_WIND_SPEED = 10.0
MSG_TXT = "{\"service client sent a message\": %.2f}"

CONNECTION_STRING_SERVICE = os.environ.get("CONNECTION_STRING_SERVICE")
print(CONNECTION_STRING_SERVICE)
DEVICE_ID = "myDevicePython"

def iothub_messaging_sample_run():
    try:
        # Create IoTHubRegistryManager
        registry_manager = IoTHubRegistryManager(CONNECTION_STRING_SERVICE)

        for i in range(0, MESSAGE_COUNT):
            print ( 'Sending message: {0}'.format(i) )
            data = MSG_TXT % (AVG_WIND_SPEED + (random.random() * 4 + 2))

            props={}
            # optional: assign system properties
            props.update(messageId = "message_%d" % i)
            props.update(correlationId = "correlation_%d" % i)
            props.update(contentType = "application/json")

            # optional: assign application properties
            props.update(testProperty = random.randint(0,1))

            registry_manager.send_c2d_message(DEVICE_ID, data, properties=props)

        input("Press Enter to continue...\n")

    except Exception as ex:
        print ( "Unexpected error {0}" % ex )
        return
    except KeyboardInterrupt:
        print ( "IoT Hub C2D Messaging service sample stopped" )


if __name__ == '__main__':
    print ( "Starting the Python IoT Hub C2D Messaging service sample..." )

    iothub_messaging_sample_run()