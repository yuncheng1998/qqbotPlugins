#-*- coding��utf-8 -*-
import urllib.request
import re
def Turning(content):
	postdata = urllib.parse.urlencode({'key':'12e3d822fdc0400b8fb79d8599dc799e','info':content}).encode('utf-8')
	req = urllib.request.Request("http://www.tuling123.com/openapi/api",postdata)
	r =  urllib.request.urlopen(req).read().decode('utf-8')
	r = r.replace('图灵机器人','Fanir')
	r1 = re.search(r'"text":"([\s\S]*)"',r)
	return r1.group(1)
def onQQMessage(bot, contact, member, content):
	# if content == '你好':
	# 	bot.SendTo(contact, str(type(contact)))
	# elif content == '哈哈':
	# 	bot.SendTo(contact,'呵呵')
	# elif re.search('年龄',content) is not None:
	# 	bot.SendTo(contact,'yes'+str(contact))
	if content == '再见':
		bot.SendTo(contact, 'close, byebye')
		bot.Stop()
	elif re.search('膜',content) is not None:
		bot.SendTo(contact,'太暴力了')
	elif re.search('苟',content) is not None:
		bot.SendTo(contact,'苟利国家生死以(滑稽)')
	elif re.search('蛤',content) is not None:
		bot.SendTo(contact,'蛤蛤')
	elif re.search('我是谁',content) is not None:
		bot.SendTo(contact,'你是'+str(contact))
	elif content is not None:
		r1 = Turning(content)
		bot.SendTo(contact,r1)