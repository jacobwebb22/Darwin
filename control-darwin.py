#!/usr/bin/python

import serial
#import binascii

port = serial.Serial("/dev/ttyAMA0", baudrate = 57600, timeout = 2)

#sit = binascii.unhexlify(''.join('ff ff fd 00 c8 07 00 03 42 00 03 00 d9 ed'.split()))
#stand = binascii.unhexlify(''.join('ff ff fd 00 c8 07 00 03 42 00 04 00 da 7f'.split()))
#forward = binascii.unhexlify(''.join('ff ff fd 00 c8 07 00 03 42 00 13 00 da 0d'.split()))
#reverse = binascii.unhexlify(''.join('ff ff fd 00 c8 07 00 03 42 00 14 00 d9 9f'.split()))
#sideleft = binascii.unhexlify(''.join('ff ff fd 00 c8 07 00 03 42 00 12 00 d9 8b'.split()))
#sideright = binascii.unhexlify(''.join('ff ff fd 00 c8 07 00 03 42 00 11 00 d9 81'.split()))
#turnleft = binascii.unhexlify(''.join('ff ff fd 00 c8 07 00 03 42 00 10 00 da 07'.split()))
#turnright = binascii.unhexlify(''.join('ff ff fd 00 c8 07 00 03 42 00 0f 00 d9 c5'.split()))
#initial = binascii.unhexlify(''.join('ff ff fd 00 c8 07 00 03 42 00 0f 00 d9 c5'.split()))
#waveleft = binascii.unhexlify(''.join('ff ff fd 00 c8 07 00 03 42 00 0e 00 da 43'.split()))
#waveright = binascii.unhexlify(''.join('ff ff fd 00 c8 07 00 03 42 00 0d 00 da 49'.split()))

#port.write(b'\xb0\xb1')
#port.close()

sit = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x03\x00\xd9\xed')
stand = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x04\x00\xda\x7f')
forward = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x13\x00\xda\x0d')
reverse = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x14\x00\xd9\x9f')
sideleft = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x12\x00\xd9\x8b')
sideright = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x11\x00\xd9\x81')
turnleft = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x10\x00\xda\x07')
turnright = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x0f\x00\xd9\xc5')
initial = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x01\x00\xda\x61')
waveleft = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x0e\x00\xda\x43')
waveright = (b'\xff\xff\xfd\x00\xc8\x07\x00\x03\x42\x00\x0d\x00\xda\x49')

port.write(initial)
port.close()
