#!/usr/bin/env python

import time
import piface.pfio as pfio

pfio.init()

print "Button 1 = Turn on relay."
print "Button 2 = Turn off relay."
print "Button 3 = Exit the script."

def checkbuttons():
        if pfio.digital_read(0) == 1:
            relayon()
        elif pfio.digital_read(1) == 1:
            relayoff()
        elif pfio.digital_read(2) == 1:
            exitscript()

def relayon():
    pfio.digital_write(1,1)
    print "Turning on relay!"
    while True:
        if pfio.digital_read(0) == 0:
            return

def relayoff():
    pfio.digital_write(1,0)
    print "Turning off relay!"
    while True:
        if pfio.digital_read(1) == 0:
            return

def exitscript():
    print "Exiting. Thanks for playing!"
    exit()

while True:
    checkbuttons()
