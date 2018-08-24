# -*- coding:utf-8 -*-
from urllib import request
from urllib import error
import re

class removeTag:
    removeImg = re.compile('<img.*?>')
    removeBlank = re.compile(' {2,}')
    removeAddr = re.compile('<a href.*?>')
    removeBr = re.compile('(?:<br>)+')
    removeOther = re.compile('<.*?>')

    def repl(self, cont):
        cont = re.sub(self.removeImg, "", cont)
        cont = re.sub(self.removeBlank, "", cont)
        cont = re.sub(self.removeAddr, "", cont)
        cont = re.sub(self.removeBr, "\n", cont)
        cont = re.sub(self.removeOther, "", cont)
        return cont.strip()

class BDTB:
    def __init__(self, baseUrl, seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.removeTag = removeTag()
        self.file = None

    def getPage(self, pageNum):
        try:
            req = request.Request(self.baseURL + self.seeLZ + '&pn=' + str(pageNum))
            resp = request.urlopen(req)
            return resp.read().decode('utf-8', 'replace')
        except error.URLError as e:
            if hasattr(e, 'reason'):
                print("Loading failed. Reason: " + e.reason)
                return None

    def getTitle(self, page):
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        title = re.findall(pattern, page)
        #print(title)
        return title

    def getPageNum(self, page):
        pattern = re.compile('<div class="pb_footer">.*?<div class="l_thread_info">.*?共<span class="red">(.*?)</span>', re.S)
        pageNum = re.findall(pattern, page)
        #print(int(pageNum[0]))
        return int(pageNum[0])

    def getContent(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            content = '\n' + self.removeTag.repl(item) + '\n'
            contents.append(content)
        return contents

    def setFile(self, title):
        fileName = title[0] + '.txt'
        print(fileName)
        if title:
            self.file = open(fileName, 'w+', encoding='utf-8')
        else:
            self.file = open('tieba.txt', 'w+')

    def writeFile(self, contents):
        for item in contents:
            self.file.write(item)

    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        #print(pageNum, title)
        contents = []
        if pageNum == None:
            print('URL invalid.')
            return

        try:
            print("%s pages in total.Title: %s" % (pageNum, title))
            self.setFile(title)
            for i in range(pageNum):
                print('Writing page %d...' % (i + 1))
                page = self.getPage(i + 1)
                contents = self.getContent(page)
                self.writeFile(contents)
        except IOError as e:
            print('IO Error. Reason: ' + e)
        finally:
            print("Writing done.")


bdtb = BDTB('http://tieba.baidu.com/p/3138733512', 1)
bdtb.start()
