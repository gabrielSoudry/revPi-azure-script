#!/usr/bin/python3

import os
import msrest
from azure.iot.hub import DigitalTwinClient

iothub_connection_str = os.getenv("CONNECTION_STRING_SERVICE")
device_id = os.getenv("IOTHUB_DEVICE_ID")

try:
    # Create DigitalTwinClient
    digital_twin_client = DigitalTwinClient(iothub_connection_str)

    # Get digital twin and retrieve the modelId from it
    digital_twin = digital_twin_client.get_digital_twin(device_id)
    if digital_twin:
        print(digital_twin)
        patch = [{"op": "add", "path": "/targetTemperature", "value": 42}]
        digital_twin_client.update_digital_twin(device_id, patch)
        print("Patch has been succesfully applied")
        # print("Model Id: " + digital_twin["$metadata"]["$model"])
    else:
        print("No digital_twin found")
except msrest.exceptions.HttpOperationError as ex:
    print("HttpOperationError error {0}".format(ex.response.text))
except Exception as exc:
    print("Unexpected error {0}".format(exc))
except KeyboardInterrupt:
    print("Sample stopped")
