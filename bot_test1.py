# -*- coding: utf-8 -*-
#!/usr/bin/python
import os
from slacker import Slacker

token = ""
try:
    token = os.environ['SLACK_BOOT_TOKEN']
except Exception as err:
    print ("[Error] %s" % (str(err)))

slack = Slacker(token)

#slack.chat.post_message('#channel', 'message')
slack.chat.post_message('#general', 'python bot test using Slacker')
