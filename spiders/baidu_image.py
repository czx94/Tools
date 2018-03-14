# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:01:58 2018

@author: Administrator
"""

import urllib.request
import re

#浏览器伪装
def pretends():
    headers = ("Uesr-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]   
    urllib.request.install_opener(opener)

#爬取函数，参数为:搜索关键词， 页数
def crawl(keyword,page):
    for k in range(0,page): 
        try:
            key = urllib.request.quote(keyword)
            url = "https://image.baidu.com/search/flip?tn=baiduimage&word="+key+"&pn="+str(k*20)
            data = urllib.request.urlopen(url).read().decode('utf-8')
            print(len(data))
            pat = '"objURL":"(.*?)",'
            rst = re.compile(pat).findall(data)

            for i in range(0,len(rst)):
                #添加异常处理
                try:
                    #获取图片扩展名
                    pat1 = '\.[^.\\/:*?"<>|\r\n]+$'
                    rst1 = re.compile(pat1).findall(rst[i])
                    #下载图片到本地
                    urllib.request.urlretrieve(rst[i],"./恐怖/"+str(k+1)+str(i)+rst1[0])
                    print('正在下载：%s' % rst[i])
                except Exception as err:
                    print(err)
        except Exception as err:
            print("出现异常:"+str(err))

def main():
    pretends()
    crawl("恐怖",30)

if __name__ == '__main__':
    main()