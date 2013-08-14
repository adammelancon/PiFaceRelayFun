#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import time
import piface.pfio as pfio
from time import gmtime, strftime

pfio.init()

#this url is the middle frame with the incident list at lafayette911.org

def get_incidents():
    url = "http://67.32.159.27/webcad/webcad.asp"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    incidents = []

    print "New Incident Loop:\n" + str(incidents)
    for i in soup.findAll('table')[1].findAll('tr'):
        incidents.append(i.get_text())
    print "=" * 20
    print strftime("%Y-%m-%d %H:%M:%S", gmtime()) # TIME

    print str(len(incidents) - 1) + " " + "Incidents" # Number of incidents
    print str(incidents) # Incident list

    incidents = []  
    print "******"
    print "Incident after clear"
    print incidents  # Should be blank
    print "******"
    
    time.sleep(5)
    get_incidents()

get_incidents()
