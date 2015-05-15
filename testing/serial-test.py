#!/usr/bin/python

# This code reads seriall data form the Darwin Bluetooh Reciever so that it can be decoded and
# manually fed back later to control the robot from the RPI.

import time
import serial

#port = serial.Serial("/dev/ttyAMA0", baudrate=57600, timeout=3.0)
port = serial.Serial("/dev/ttyAMA0", baudrate=57600)

for i in range(1,30):
#    rcv = port.read(20)
#    print rcv
    rcv = port.read(14)
    hexout = ':'.join(x.encode('hex') for x in rcv)
    print hexout
    time.sleep(0.5)   # sleep in seconds
# end for

port.close()
