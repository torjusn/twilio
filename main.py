# -----------------------------------------------------------
# sends sms alerts w/ twilio depending on sql db values
#
# Torjus Nilsen, Kongsberg, Norway
# email tornil1996@hotmail.com
# -----------------------------------------------------------

#
import os
from twilio.rest import Client

###
# CONNECT TO SQL DB
###

'''
user="postgres",
password="",
host="127.0.0.1",
port="5432",
database="dvdrental"
'''


###
# TWILIO SMS ALERT
###