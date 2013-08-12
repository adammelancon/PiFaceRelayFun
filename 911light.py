#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import time
import piface.pfio as pfio

pfio.init()

#this url is the middle frame with the incident list at lafayette911.org
url = "http://67.32.159.27/webcad/webcad.asp"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

# A class to controll the relay
class Bpress:
    def relayon(self):
        pfio.digital_write(1,1)
        print "Turning on relay!"
        while True:
            if pfio.digital_read(0) == 0:
                return

    def relayoff(self):
        pfio.digital_write(1,0)
        print "Turning off relay!"
        while True:
            if pfio.digital_read(1) == 0:
                return

    def exitscript(self):
        pfio.digital_write(1,0)
        print "Exiting. Thanks for playing!"
        exit()

piface = Bpress()

# Relay Test
#piface.relayon()
#time.sleep(3)
#piface.relayoff()



def get_incidents():
    # Create an emapty list for incidents
    incidents = []
    lookfor = "JOHNSTON"

    # Find the second table which has the incidents and find the individual row$
    for i in soup.findAll('table')[1].findAll('tr'):
        incidents.append(i.get_text()) # Add the text from the row to the list
    
    # Give it a road to look for incidents on to trigger the led.
    if filter(lambda x: lookfor in x,incidents):
        print "Incident reported on" + " " + lookfor
        piface.relayon()
    else:
        print "No incidents on" + " " + lookfor
        piface.relayoff()
    time.sleep(30)

while True:
    get_incidents()
    if pfio.digital_read(0) == 1:
        piface.relayoff()
        exit()
