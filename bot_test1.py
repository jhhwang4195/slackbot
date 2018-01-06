from slacker import Slacker

token = 'Your_Bot_Token'
slack = Slacker(token)

#slack.chat.post_message('#channel', 'message')
slack.chat.post_message('#general', 'python bot test using Slacker')
