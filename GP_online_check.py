import requests
import re
from lxml import etree


headers = {
    'Referer': 'https://play.google.com/store/apps',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}

pkg = input("请输入包名，以逗号分隔：")
pkg_list = re.findall(r"[a-zA-Z0-9.]+", pkg)
print(pkg_list)


for p in pkg_list:
    print('Checking %s' %p)
    response = requests.get('https://play.google.com/store/apps/details?id=' + p, headers=headers)
    html = etree.HTML(response.text)
    print(html.xpath('//head/title/text()'))