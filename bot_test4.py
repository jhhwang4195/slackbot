# -*- coding: utf-8 -*-
#!/usr/bin/python
import os
import time
from slacker import Slacker

token = ""
try:
    token = os.environ['SLACK_BOOT_TOKEN']
except Exception as err:
    print ("[Error] %s" % (str(err)))

slack = Slacker(token)
channel = "#monitoring"

commands = ('uptime',
            'df -h',
            'free -m',
            'netstat -ant | grep ESTABLISH',
            )

print time.strftime("%Y-%m-%d %H:%M")

slack.chat.post_message(channel, '##################################################')
title = "*System Monitoring: %s*" % time.strftime("%Y-%m-%d %H:%M:%S")
slack.chat.post_message(channel, title)

for command in commands:
    input_command = ""
    input_command = "> command: %s" % command
    result = os.popen(command)
    slack.chat.post_message(channel, input_command)
    slack.chat.post_message(channel, '```' + result.read() + '```')
