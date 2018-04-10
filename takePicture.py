from subprocess import call
from slackNotifications import *

call(["./webcam.sh"], shell=True)

send_message('notifications','picture taken')

