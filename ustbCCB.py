import urllib.request
import http.cookiejar
import sys
import getpass
import re

url = "http://e.ustb.edu.cn/userPasswordValidate.portal"#登陆url
data={}#表单
data['Login.Token1']=input("账号")
data['Login.Token2']=getpass.getpass("密码")
data['goto']=r'http://e.ustb.edu.cn/loginSuccess.portal'
data['gotoOnFail']=r'http://e.ustb.edu.cn/loginFailure.portal'
headers = {'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
			r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3'}

url = "http://e.ustb.edu.cn/userPasswordValidate.portal"

data = {}
data['Login.Token1'] = input("账号")
data['Login.Token2'] = getpass.getpass("密码")
data['goto'] = r'http://e.ustb.edu.cn/loginSuccess.portal'
data['gotoOnFail'] = r'http://e.ustb.edu.cn/loginFailure.portal'
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')


def saveCookie(url, data):
	cj = http.cookiejar.CookieJar()
	opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
	r = opener.open(url, data)
	return cj

# 利用cookie登陆返回余额
def bill(cj):
	str = ""
	handler = urllib.request.HTTPCookieProcessor(cj)
	opener = urllib.request.build_opener(handler)
	get_url = 'http://e.ustb.edu.cn/index.portal?.pn=p378_p381'
	get_request = urllib.request.Request(get_url)
	get_response = opener.open(get_request)
	htmlmessage = get_response.read().decode('utf-8').replace(' ', '').replace('\t', '').replace('\r\n\r\n', '')
	#使用正则表达式时注意已经代替了空白字符
	money = re.search(r'<tdalign="center">(.\n*)*?</table>', htmlmessage)
	cost = re.findall(r'class="table_text[\d]{0,1}">((.*)*?)</td>', htmlmessage)
	
	i = 0
	while i < 29:
		str = str + cost[i][0] + ', '
		# print(cost)
		if((i + 1) % 4 == 0 ):
			str = str + '///'
		i = i + 1
	return str

str = (bill(saveCookie(url, data)))

def onQQMessage(bot, contact, member, content):
	if content == r'/消费':
		bot.SendTo(contact, str)
