import os
import time
from slacker import Slacker

token = 'Your_Bot_Token'
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
	slack.chat.post_message(channel, '```'+ result.read() + '```')
