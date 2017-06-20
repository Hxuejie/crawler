# coding=gbk

import urllib2
import re

class HtmlFile:
    "Html文件"
    __url = ""  # html路径
    __data = "" # 文件数据
    __links = []# 文件内所有链接

    # 构建
    def __init__(self, url):
        self.__url = url
        print "创建Html文件: ", self.__url

    # 下载
    def download(self):
        if self.__data == "" :
            print "下载Html文件: ", self.__url
            self.__data = urllib2.urlopen(urllib2.Request(self.__url)).read()
        else :
            print "Html文件已下载过了"

    # 获取html数据
    def getData(self):
        return self.__data

    # 保存到文件
    def save(self, path):
        print "保存Html文件到: ", path
        url = self.__url
        if url.find("?") != -1:
            fname = url.rpartition("?")[0].rpartition("/")[2]
        else:
            fname = url.rpartition("/")[2]
        if fname == "":
            fname = url.partition("//")[2].partition("/")[0] + ".html"
        print "文件名: ", fname
        f = open(path + "/" + fname, "wb")
        f.write(self.__data)
        f.close()

    # 获取文件内所有链接
    def getLinks(self):
        if len(self.__links) > 0:
            return self.__links
        else:
            self.__parseLinks()
            return self.__links

    # 解析链接
    def __parseLinks(self):
        if self.__data == "" :
            return
        ret = re.finditer(r"<a.*?href=\"(http.*?)\".*?/a>", self.__data, re.M|re.I)
        if ret:
            for r in ret:
                self.__links.append(r.group(1))        
        
