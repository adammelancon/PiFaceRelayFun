#!/usr/bin/env python
#This script controls the piface relays from the keyboard.
#It controls the built-in relay which is hooked up to a small motor or light.

import piface.pfio as pfio

pfio.init()

print "A = Turn on relay."
print "B = Turn off relay."
print "C = Exit the script."

def checkbuttons():
    decide = raw_input("Enter your selection: ")
    if decide.lower() == "a":
        relayon()
    elif decide.lower() == "b":
        relayoff()
    elif decide.lower() == "c":
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
