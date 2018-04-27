import urllib.request
import re


def Turning(content):
    url = "http://www.tuling123.com/openapi/api"
    postdata = urllib.parse.urlencode({
        'key': '12e3d822fdc0400b8fb79d8599dc799e',
        'info': content
    }).encode('utf-8')

    response = urllib.request.urlopen(url, postdata)
    html = response.read().decode('utf-8')
    r1 = re.search(r'"text":"([\s\S]*)"', html)
    return r1.group(1)


def onQQMessage(bot, contact, member, content):
    if content == '再见':
        bot.SendTo(contact, 'close, byebye')
        bot.Stop()
    elif re.search('索思', content) is not None:
        bot.SendTo(contact, '索思科技协会')
    elif re.search('我是谁', content) is not None:
        bot.SendTo(contact, '你是' + str(contact))
    elif re.match('/help', content) is None:
        if re.search('#', content) is None:
            if re.search('/消费',content) is None:  # 借书命令
                r1 = Turning(content)  # 调用图灵机器人
                bot.SendTo(contact, r1)
