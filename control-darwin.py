#!/usr/bin/python

import serial
port = serial.Serial("/dev/ttyAMA0", baudrate = 57600, timeout = 2)
port.write(b'\xb0\xb1')
port.close()
