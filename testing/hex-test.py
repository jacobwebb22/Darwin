#!/usr/bin/python

# This code is used to attempt to parse the serial hex data from darwin to write it back later

import binascii

out = binascii.unhexlify(''.join('ff ff fd 00 c8 07 00 03 42 00 03 00 d9 ed'.split()))
print out

hexout = ':'.join(x.encode('hex') for x in out)
print hexout


