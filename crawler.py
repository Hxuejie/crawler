#coding=gbk

import urllib2
from htmlFile import *
from vcImage import *

url = "http://doc.zx35.com/doc/index.php?s=/home/item/pwd/item_id/12"
savePath = "C:\\Users\\Hxuejie\\Desktop\\doc"
print "根地址:", url

hf = HtmlFile(url)
hf.download()
hf.save(savePath)
for l in hf.getLinks():
    hf = HtmlFile(l)
    hf.download()
    hf.save(savePath)

vc = VCImage("http://doc.zx35.com/doc/Public/verifyCode.php")
vc.download()
print vc.getCode(False)
