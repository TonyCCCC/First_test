# -*- coding:utf-8 -*-

from urllib import request
from urllib import error
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
referer = url
headers = {
    'User-Agent': user_agent
}

try:
    req = request.Request(url, headers=headers)
    resp = request.urlopen(req)
    result = resp.read().decode('utf-8', 'replace')
except error.URLError as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)

pattern = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">\n<span>(.*?)</span>(.*?)<i class="number">(.*?)</i>', re.S)
items = re.findall(pattern, result)
f = open('qiushibaike.txt', 'w', encoding='utf-8')
text = ""
for cont in items:
    if not re.findall('<img', cont[2]):
        text += "%s\n%s\n%s"%(cont[0], cont[1], cont[3])
    else:
        pass
f.write(text)
f.close()