#Light Control
#Controls the turning on and turning off of lights
#Lights are wired into Relay #4 (Pin 29)

from slackNotifications import *
from Relay import *

def setLightOn(test=False):
    "Check the time (scheduleCron.py does this) and determine if the lights need to be changed"
    relay = Relay()
    state=relay.getState(lightPin)
    on = True
    if state is not on:
        print('set light on')
        send_message('notifications','set light on')
        relay.setOn(lightPin)

# Im not using this
def logState(value, test=False):
    status_qualifier='Success'
    if test:
        status_qualifier='Test'
    jsn=makeEnvJson('State_Change', 'Lights', 'Top', 'State', value, 'Lights', status_qualifier)
    CouchDB.logEnvObsvJSON(jsn)

def test():
    print("Test Lights On")
    setLightOn(True)

##if __name__=="__main__":
##    setLightOn()    
    
setLightOn()

