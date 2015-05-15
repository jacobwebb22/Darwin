#!/usr/bin/python

import serial
import os
import sys
import termios
import tty

# Initialize Serial Port

#port = serial.Serial("/dev/ttyAMA0", baudrate = 57600, timeout = 0.5)
port = serial.Serial("/dev/ttyAMA0", baudrate = 57600)

sit = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x03\x00\xd9\xed')
stand = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x02\x00\xda\x6b')
forward = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x13\x00\xda\x0d')
reverse = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x14\x00\xd9\x9f')
sideleft = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x12\x00\xd9\x8b')
sideright = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x11\x00\xd9\x81')
turnleft = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x10\x00\xda\x07')
turnright = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x0f\x00\xd9\xc5')
initial = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x01\x00\xda\x61')
waveleft = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x0e\x00\xda\x43')
waveright = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x0d\x00\xda\x49')
fastadvance = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x27\x00\xd9\x35')
stopadvance = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x00\x00\xd9\xe7')

# Get Keypress Function

def getKey():
   fd = sys.stdin.fileno()
   old = termios.tcgetattr(fd)
   new = termios.tcgetattr(fd)
   new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
   new[6][termios.VMIN] = 1
   new[6][termios.VTIME] = 0
   termios.tcsetattr(fd, termios.TCSANOW, new)
   key = None
   try:
      key = os.read(fd, 3)
   finally:
      termios.tcsetattr(fd, termios.TCSAFLUSH, old)
   return key

# Main Loop

while 1:
	x = str(getKey())
	if x == "p":
		port.close()
		break
	if x == "i":
		port.write(initial)
		print(x)
	if x == "w":
		port.write(forward)
		print(x)
	if x == "a":
		port.write(sideleft)
		print(x)
	if x == "s":
		port.write(reverse)
		print(x)
        if x == "d":
                port.write(sideright)
		print(x)
        if x == "q":
                port.write(turnleft)
		print(x)
        if x == "e":
                port.write(turnright)
		print(x)
        if x == "t":
                port.write(waveleft)
		print(x)
        if x == "y":
                port.write(waveright)
		print(x)
        if x== "u":
                port.write(stand)
                print(x)
#        if x == "":
#                port.write()
