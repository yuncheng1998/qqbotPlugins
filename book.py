import re
import urllib.request

def book(operate,findbook):
	html = urllib.request.urlopen('http://blog.csdn.net/dd864140130/article/details/54991817').read().decode('utf-8')
	index = re.findall('<td><ul>([\s\S]*?)</ul></td>',str(html))
	if operate == 1: # 列出书单
		booklist = []
		for i in index:
			book = re.findall('\\w*|\\W*|[\\u4e00-\\u9fa5]',i)
			booklist.append(book[6])
		return booklist
	if operate == 2: # 书籍查询
		booklist = []
		for i in index:
			result = re.search(findbook,i)
			book = re.findall('\\w*|\\W*|[\\u4e00-\\u9fa5]',i)
			if result is not None:
				booklist.append(book[6])
		return booklist
def onQQMessage(bot, contact, member, content):
	if re.search('#',content) is not None:
		if re.search('书单',content) is not None:
			bot.SendTo(contact,str(book(1,None)))
		if re.search('找书',content) is not None:
			b = re.findall('%(.*?)%',content)[0]
			if b is not None:
				bot.SendTo(contact,str(book(2,b)))	
			elif b is None:
				bot.SendTo(contact,'没有')



