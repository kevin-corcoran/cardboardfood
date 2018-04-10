# Author: Howard Webb
# Data: 7/25/2017
# Fan actuator controlled by thermometer

from thermostat import adjustThermostat

# desired temperature range
low = 70
high = 80
try:
    adjustThermostat(low,high)  
except IOError as e:
    print("Failure to get temperature, no sensor found; check pins and sensor")

  
    
