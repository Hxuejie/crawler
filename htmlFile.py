# coding=gbk

import urllib2
import re

class HtmlFile:
    "Html�ļ�"
    __url = ""  # html·��
    __data = "" # �ļ�����
    __links = []# �ļ�����������

    # ����
    def __init__(self, url):
        self.__url = url
        print "����Html�ļ�: ", self.__url

    # ����
    def download(self):
        if self.__data == "" :
            print "����Html�ļ�: ", self.__url
            self.__data = urllib2.urlopen(urllib2.Request(self.__url)).read()
        else :
            print "Html�ļ������ع���"

    # ��ȡhtml����
    def getData(self):
        return self.__data

    # ���浽�ļ�
    def save(self, path):
        print "����Html�ļ���: ", path
        url = self.__url
        if url.find("?") != -1:
            fname = url.rpartition("?")[0].rpartition("/")[2]
        else:
            fname = url.rpartition("/")[2]
        if fname == "":
            fname = url.partition("//")[2].partition("/")[0] + ".html"
        print "�ļ���: ", fname
        f = open(path + "/" + fname, "wb")
        f.write(self.__data)
        f.close()

    # ��ȡ�ļ�����������
    def getLinks(self):
        if len(self.__links) > 0:
            return self.__links
        else:
            self.__parseLinks()
            return self.__links

    # ��������
    def __parseLinks(self):
        if self.__data == "" :
            return
        ret = re.finditer(r"<a.*?href=\"(http.*?)\".*?/a>", self.__data, re.M|re.I)
        if ret:
            for r in ret:
                self.__links.append(r.group(1))        
        
