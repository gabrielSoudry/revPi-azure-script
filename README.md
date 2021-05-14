# Revolution Pi and Azure 

## Hardware

- [RevPi Core 3+](https://revolution.kunbus.com/revpi-core/)
- [Revpi Digital IO modules](https://revolution.kunbus.com/io-modules/)

## Libraries 

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-360/)

- [Azure Iot Sdk Python](https://github.com/Azure/azure-iot-sdk-python)
- [Revpimodio2](https://github.com/naruxde/revpimodio2)

## Project structure
- ![directory](https://github.com/tpierrain/cqrs/blob/master/images/directory.png?raw=true) __**Device**__: Code hosted on the RevPi
- ![directory](https://github.com/tpierrain/cqrs/blob/master/images/directory.png?raw=true) __Service__: Code hosted on Microsoft Azure

## Setup

We will need first to setup several env variable. The most easy way to do it, it's to create a .env file at the root level:

```bash
export CONNECTION_STRING_DEVICE=<HostName=...;DeviceId=...;SharedAccessKey=...>
export CONNECTION_STRING_SERVICE=<HostName...net;SharedAccessKeyName=...;SharedAccessKey=....">
```
And then source it: 
```bash
$ source .env
```

Now you can execute all python script


## Useful links:
Azure : 
- [Azure Iot hub Sdk python Device Sample](https://github.com/Azure/azure-iot-sdk-python/tree/master/azure-iot-device/samples/async-hub-scenarios)
- [Azure Iot hub Sdk python Service Sample](https://github.com/Azure/azure-iot-sdk-python/tree/master/azure-iot-hub/samples)

Revpi dio :
 - [Tutorial DIO Module](https://www.rs-online.com/designspark/getting-started-with-the-versatile-revolution-pi-modular-industrial-platform)
 
