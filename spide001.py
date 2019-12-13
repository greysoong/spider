# -*- coding: UTF-8 -*-
"""
file:spide001.py
data:2019-12-109:39
author:Grey
des:
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime,random

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    print("http://en.wikipedia.org" + articleUrl)
    html = urlopen("http://en.wikipedia.org"+articleUrl)

    bsObj = BeautifulSoup(html)
    return bsObj.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$'))
links = getLinks('/wiki/Kevin_Bacon')
while len(links)>0:
    newArticle = links[random.randint(0,len(links)-1)].attrs['href']
    print(newArticle)
    links=getLinks(newArticle)

