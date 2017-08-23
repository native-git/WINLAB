#!/usr/bin/env python

import smtplib
import os

ip_addr = os.popen('hostname -I').read()
host = os.popen('hostname').read()
message = "Subject: Remote System Bootup for: " + host
message += "Ip address for remote system: "+ str(ip_addr)

smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.ehlo()

smtpObj.starttls()
smtpObj.login('nativeremote@gmail.com','native101')
smtpObj.sendmail('nativeremote@gmail.com','mjs695@rutgers.edu',message)
smtpObj.quit()
