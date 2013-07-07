#!/usr/bin/env python
#This script controls buttons 0, 1, and 2, which are built into the Piface.
#It controls the built-in relay which is hooked up to a small motor or light.
#testing git commit

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
    pfio.digital_write(1,0)
    print "Exiting. Thanks for playing!"
    exit()

while True:
    checkbuttons()
