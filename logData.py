#!bin/env python
from datetime import datetime
import json
from si7021 import *
import os
import time
from slackNotifications import *

class logData():
    initialized = False
    def __init__(self):
        f = open('/home/pi/PMVP/data.txt','r')
        if os.stat('/home/pi/PMVP/data.txt').st_size == 0: # file is empty
            self.initialize()
        else:
            self.data = json.load(f)
        f.close()
        # but note we still need this line
        self.si = si7021()
    
    def initialize(self):
        self.data = {}
        self.data['date'] = []
        self.data['temperature'] = []
        self.data['humidity'] = []
    
    def logData(self):
        """ load json data and log new data readings; date/time, temperature and humidity.
            and add to data.txt file
            json allows us to load data as a dictionary. """
        
##        with open('data.txt') as json_file:
##            data = json.load(json_file)
        currentDT = datetime.now()
        self.data['date'].append({
                    'month': currentDT.month,
                    'day': currentDT.day,
                    'year': currentDT.year,
                    'hour': currentDT.hour,
                    'minute': currentDT.minute,
                    'second': currentDT.second
        })
        # for some reason my sensor sometimes records temperatures in the negative when its obviously not true
        # so give sensor two chances to get it right!
        self.count = 0; self.temp = self.si.getTempF()
        while self.temp < 0 and self.count < 2:
            self.temp = self.si.getTempF()
            self.count += 1
        if self.temp > 0: # dont log if its negative
            self.data['temperature'].append({
    ##                    'tempF' : abs(self.si.getTempF())
                'tempF' : self.temp
            })
        self.data['humidity'].append({
                    'humidity' : self.si.getHumidity()
        })
        # write to text file
        with open("data.txt","w") as outfile:
            json.dump(self.data,outfile)
            
if __name__=="__main__":
    log = logData()
    log.logData()
    send_message(notify,'data logged')
# This gets logged to a txt file, and I dont think we need notifications
