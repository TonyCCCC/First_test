import requests
from bs4 import BeautifulSoup
from lxml import etree

class getIndex:

    def get(self):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0'
        }
        url = 'http://www.zhihu.com/api/v4/columns/crossin/articles?limit=10&offset=0'
        offset = 0
        index = {}
        while 1:
            print('Opening %s' %url)
            response = requests.get(url, headers=headers)
            print(response)
            offset += 10
            page = response.json()
            data = page['data']
            for article in data:
                index[article['id']] = article['title']
            if page['paging']['is_end'] == True:
                break
            url = page['paging']['next']

        return index


class getContent:

    def __init__(self):
        index = getIndex()
        self.index = index.get()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0'
        }

    def get(self):
        index = self.index
        for id in list(index.keys()):
            filename = "C:/Users/Administrator/PycharmProjects/First_test/zhihu/" + str(id) + ".txt"
            url = 'https://zhuanlan.zhihu.com/p/' + str(id)
            content = ""
            print('Opening article %s' %index[id])
            response = requests.get(url, headers=self.headers).content
            html = etree.HTML(response)
            article = html.xpath('//div[@class="RichText ztext Post-RichText"]//text()')
            for para in article:
                content += para
                content += '\n'
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)


if __name__ == '__main__':
    a = getContent()
    a.get()