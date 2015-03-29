#!/usr/bin/python

import time
import serial

port = serial.Serial("/dev/ttyAMA0", baudrate=57600, timeout=2.0)

for i in range(1,10):
    rcv = port.read(10)
    print rcv
    time.sleep(0.5)   # sleep in seconds
# end for

port.close()
