#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import time
import piface.pfio as pfio
from time import gmtime, strftime

pfio.init()

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

piface = Bpress()

# Relay Test
#piface.relayon()
#time.sleep(3)
#piface.relayoff()



def get_incidents():
    url = "http://67.32.159.27/webcad/webcad.asp"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    incidents = []

    # Find the second table which has the incidents and find the individual row.
    try:
        lookfor = "AMBASSADOR" # What street to light up for.
        for i in soup.findAll('table')[1].findAll('tr'):
            incidents.append(i.get_text()) # Add the text from the row to the incidents list

    except IndexError:
        print "=" * 20
        print "No incidents on" + " " + lookfor
        #piface.relayoff()
        print strftime("%Y-%m-%d %H:%M:%S", gmtime())
        print str(len(incidents) - 1) + " " + "Incidents"
        print str(incidents)
    
    if filter(lambda x: lookfor in x,incidents):
        print "=" * 20
        print "Incident reported on" + " " + lookfor
       #piface.relayon()
        print strftime("%Y-%m-%d %H:%M:%S", gmtime())
        print str(len(incidents) - 1) + " " + "Incidents"
        print str(incidents)
    
    else:
        print "=" * 20
        print "No incidents on" + " " + lookfor
       #piface.relayoff()
        print strftime("%Y-%m-%d %H:%M:%S", gmtime())
        print str(len(incidents) - 1) + " " + "Incidents"
        print str(incidents)

    time.sleep(10)

while True:
    get_incidents()
    #if pfio.digital_read(0) == 1:
    #    piface.relayoff()
    #    exit()
