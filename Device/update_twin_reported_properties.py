#!/usr/bin/python3

from azure.iot.device.aio import IoTHubDeviceClient
import random
import asyncio
import os


async def main():
    conn_str = os.getenv("CONNECTION_STRING_DEVICE")
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    # connect the client.
    await device_client.connect()

    # update the reported properties
    reported_properties = {"temperature": random.randint(320, 800) / 10}
    print("Setting reported temperature to {}".format(
        reported_properties["temperature"]))
    await device_client.patch_twin_reported_properties(reported_properties)

    # Finally, shut down the client
    await device_client.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
