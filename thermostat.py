#thermostat.py
#controlls the exhaust fan, turns it on when temperature is over the target temperature
#Fan is assumed to be wired to Pin 33 (GPIO 13)
#Pin 30 may control a relay or be a transistor switch, assumes HIGH means ON

from si7021 import *
from Relay import *
from slackNotifications import *

def adjustThermostat(low,high):
    """Turn the fan on or off in relationship to target temperature range / and time of day?"""
    si = si7021()
    relay = Relay()
    
    temp = si.getTempF()
    relay.setOn(fanPin)
    state=relay.getState(fanPin)
    on_ = True; off_ = False
    
    if state is on_ and temp < low: 
        print('turn fan off')
        send_message('notifications','turn fan off')
        relay.setOff(fanPin)
        state = off_
    if state is off_ and temp > high:
        print('turn fan on')
        send_message('notifications','turn fan on')
        relay.setOn(fanPin)
        state = on_
        
    print(temp)
    # display state
    if state is on_:
        print('fan is on')
    else:
        print('fan is off')


