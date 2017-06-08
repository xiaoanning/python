#coding=utf-8
import urllib
import re

def getHtml(url):
	page = urllib.urlopen(url) #打开URL
	html = page.read() #读取数据
	return html


def getImg(html):
	reg = r'src="(.+?\.png|\.jpg)"'
	imgre = re.compile(reg) #将正则表达式对象化
	imglist = re.findall(imgre,html) #查找所有符合正则表示的值

	x = 0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,'%s.png' %x) #将远程数据下载到本地
		x += 1 
    

#html = getHtml("https://tieba.baidu.com/index.html")
#html = getHtml("http://map.baidu.com/?newmap=1&ie=utf-8&s=s%26wd%3D杭州银行")
#html = getHtml("http://webmap0.map.bdstatic.com/wolfman/static/common/pkg/init-pkg_d0fbac8.js")
#html = getHtml("http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=ͼƬ&fr=ala&ala=1&alatpl=others&pos=0")
html = getHtml("http://www.cnblogs.com/fnng/p/3576154.html")
#html = getHtml("https://hyzx.hzbank.com.cn:444/HzBankOnlineServer/service/version/queryVersionInfo.do?platform=iPhone")

#print getImg(html)
print html
