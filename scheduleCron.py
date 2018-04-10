from crontab import CronTab
##import time

# run $ chmod u=rwx scheduleCron.py
# in the terminal to allow proper permissions.
cron = CronTab(user='pi') 
for job in cron:
   cron.remove(job)
# cron jobs
adjustThermostat = cron.new(command='python3 /home/pi/PMVP/adjustThermostat.py',comment='adjustThermostat')
setLightOn = cron.new(command='python3 /home/pi/PMVP/setLightOn.py',comment='setLightOn')
setLightOff = cron.new(command='python3 /home/pi/PMVP/setLightOff.py',comment='setLightOff')
logData = cron.new(command='/home/pi/PMVP/logData.sh',comment='logData')
takePicture = cron.new(command='/home/pi/PMVP/webcam.sh',comment='takePicture')

# check thermostat every minute
adjustThermostat.minute.every(1)
# log data every 20 minute
logData.minute.every(20)
# set lights on at 6 am
setLightOn.hour.on(6)
# set lights off at 10 pm
setLightOff.hour.on(22)
# take a picture every hour between 6 am and 10 pm ?
# doesnt work, manually edited with crontab -e in terminal to run every 2 hours between
# 6 am and 10pm
# 0 6-22/2 * * * [command] 
takePicture.hour.during(6,22)

cron.write()
