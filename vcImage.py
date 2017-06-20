# coding=gbk

import urllib2
from PIL import Image
from pytesser import *
import io  
import ImageEnhance    
import ImageFilter    
import sys

# 二值化    
threshold = 140    
table = []    
for i in range(256):    
    if i < threshold:    
        table.append(0)    
    else:    
        table.append(1)    
    
#由于都是数字    
#对于识别成字母的 采用该表进行修正    
rep={'O':'0',    
    'I':'1','L':'1',    
    'Z':'2',    
    'S':'8'    
    }; 

class VCImage:
    "图片验证码"
    __url = ""  # 验证码URL
    __code = "" # 验证码
    __image = ""# 图片

    def __init__(self, url):
        self.__url = url

    # 下载验证码
    def download(self):
        print "下载验证码: ", self.__url
        data = urllib2.urlopen(urllib2.Request(self.__url)).read()
        self.__image = Image.open(io.BytesIO(data)).convert('L')

    # 获取验证码
    def getCode(self, auto=True):
        if not auto:
            self.__inputCode()
        else:
            if self.__code =="":
                self.__pauseCode()
        return self.__code;

    # 手动输入验证码
    def __inputCode(self):
        self.__image.show()
        self.__code = input("输入验证码:\n")

    # 解析验证码
    def __pauseCode(self):
        #二值化，采用阈值分割法，threshold为分割点
        out = self.__image.point(table,'1')
        self.__code = image_to_string(out)
        self.__code.strip()
        self.__code.upper()
        for r in rep:    
            self.__code = self.__code.replace(r,rep[r]) 
        print "解析验证码: ", self.__code
        
