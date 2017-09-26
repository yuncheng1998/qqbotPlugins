import re

#helpDict

help =  '列出书单 --- #书单\n找书 --- #找书%书的名字(部分即可)%\n校园卡消费 --- /消费'

def onQQMessage(bot, contact, member, content):
	if content == r'/help':
		bot.SendTo(contact,help)
