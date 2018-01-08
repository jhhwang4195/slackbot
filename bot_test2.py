# -*- coding: utf-8 -*- 
import os
from slacker import Slacker

token = 'Your_Bot_Token'
slack = Slacker(token)

attachments_dict = dict()
attachments_dict['pretext'] = "attachments 블록 전에 나타나는 text"
attachments_dict['title'] = "다른 텍스트 보다 크고 볼드되어서 보이는 title"
attachments_dict['title_link'] = "jhhwang4195.tistory.com"
attachments_dict['fallback'] = "클라이언트에서 노티피케이션에 보이는 텍스트 입니다. attachment 블록에는 나타나지 않습니다"

p = os.popen('df -h')
attachments_dict['text'] = p.read()
attachments_dict['mrkdwn_in'] = ["text", "pretext"]  # 마크다운을 적용시킬 인자들을 선택합니다.
attachments = [attachments_dict]

slack.chat.post_message(channel="#general", text=None, attachments=attachments)
slack.chat.post_message(channel="#monitoring", text=None, attachments=attachments)
