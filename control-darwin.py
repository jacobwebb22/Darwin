#!/usr/bin/python

import serial
port = serial.Serial("/dev/ttyAMA0", baudrate = 57600, timeout = 2)
port.write("message to send")
port.close()
