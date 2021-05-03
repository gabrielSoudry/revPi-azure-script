#!/usr/bin/python3

# Tuto link : https://www.rs-online.com/designspark/getting-started-with-the-versatile-revolution-pi-modular-industrial-platform

import revpimodio2
import time

revpi = revpimodio2.RevPiModIO(autorefresh=True)

revpi.io.Relay.value = True

time.sleep(2)

revpi.io.Relay.value = False

revpi.exit()