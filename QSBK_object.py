# -*- coding:utf-8 -*-
from urllib import request
from urllib import error
import re

class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.userAgent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0'
        self.headers = {'User-Agent': self.userAgent}
        self.stories = []
        self.switch = False

    def getPage(self, pageIndex):
        try:
            url = "https://www.qiushibaike.com/hot/page/" + str(pageIndex)
            reqst = request.Request(url, headers=self.headers)
            resp = request.urlopen(reqst)
            pageCont = resp.read().decode('utf-8', 'replace')
            return pageCont
        except error.URLError as e:
            print("Connection failed. Reason: " + e.reason)
            return None

    def getItem(self, pageIndex):
        pageCont = self.getPage(pageIndex)
        if not pageCont:
            print("Content loading failed.")
            return None
        else:
            pattern = re.compile(
                r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">\n<span>(.*?)</span>(.*?)<i class="number">(.*?)</i>',
                re.S)
            pageItems = re.findall(pattern, pageCont)
            pageStories = []
            for item in pageItems:
                if not re.search('img', item[2]):
                    replaceBR = re.compile('<br/>')
                    text = re.sub(replaceBR, '\n', item[1])
                    pageStories.append([item[0].strip(), text.strip(), item[3].strip()])
        return pageStories

    def loadPage(self):
        if len(self.stories) < 2 and self.switch == True:
            pageStories = self.getItem(self.pageIndex)
            if pageStories:
                self.stories.append(pageStories)
                self.pageIndex += 1

    def prtItem(self, pageStories):
        for item in pageStories:
            inp = input()
            if inp == "Q":
                self.switch = False
                print('Sucessfully exit.')
                return None
            print('第%s页\t作者:%s\t评论:%s\n%s'%(self.pageIndex - 1, item[0], item[2], item[1]))

    def start(self):
        print("Loading...\nInput Enter to get a story. Input Q to quit.")
        self.switch = True
        self.loadPage()
        while self.switch:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                del self.stories[0]
                self.prtItem(pageStories)
                self.loadPage()

spider = QSBK()
spider.start()
