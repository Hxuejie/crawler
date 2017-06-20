# coding=gbk

import urllib2
from PIL import Image
from pytesser import *
import io  
import ImageEnhance    
import ImageFilter    
import sys

# ��ֵ��    
threshold = 140    
table = []    
for i in range(256):    
    if i < threshold:    
        table.append(0)    
    else:    
        table.append(1)    
    
#���ڶ�������    
#����ʶ�����ĸ�� ���øñ��������    
rep={'O':'0',    
    'I':'1','L':'1',    
    'Z':'2',    
    'S':'8'    
    }; 

class VCImage:
    "ͼƬ��֤��"
    __url = ""  # ��֤��URL
    __code = "" # ��֤��
    __image = ""# ͼƬ

    def __init__(self, url):
        self.__url = url

    # ������֤��
    def download(self):
        print "������֤��: ", self.__url
        data = urllib2.urlopen(urllib2.Request(self.__url)).read()
        self.__image = Image.open(io.BytesIO(data)).convert('L')

    # ��ȡ��֤��
    def getCode(self, auto=True):
        if not auto:
            self.__inputCode()
        else:
            if self.__code =="":
                self.__pauseCode()
        return self.__code;

    # �ֶ�������֤��
    def __inputCode(self):
        self.__image.show()
        self.__code = input("������֤��:\n")

    # ������֤��
    def __pauseCode(self):
        #��ֵ����������ֵ�ָ��thresholdΪ�ָ��
        out = self.__image.point(table,'1')
        self.__code = image_to_string(out)
        self.__code.strip()
        self.__code.upper()
        for r in rep:    
            self.__code = self.__code.replace(r,rep[r]) 
        print "������֤��: ", self.__code
        
