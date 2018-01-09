# -*- coding: utf-8 -*-
#!/usr/bin/python
import os
from slacker import Slacker

token = ""
try:
    token = os.environ['SLACK_BOT_TOKEN']
except Exception as err:
    print ("[Error] %s" % (str(err)))

slack = Slacker(token)

slack.chat.post_message('#monitoring', '>-------------------------------------')
slack.chat.post_message('#monitoring', '*System Monitoring*')

slack.chat.post_message('#monitoring', '> command: uptime')
p = os.popen('uptime')
slack.chat.post_message('#monitoring', '```' + p.read() + '```')

slack.chat.post_message('#monitoring', '> command: df -h')
p = os.popen('df -h')
slack.chat.post_message('#monitoring', '```' + p.read() + '```')

slack.chat.post_message('#monitoring', '> command: free -m')
p = os.popen('free -m')
slack.chat.post_message('#monitoring', '```' + p.read() + '```')

slack.chat.post_message('#monitoring', '> command: netstat -ant | grep ESTABLISH')
p = os.popen('netstat -ant | grep ESTABLISH')
slack.chat.post_message('#monitoring', '```' + p.read() + '```')
