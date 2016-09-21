#coding:utf8 
from urllib.request import urlopen
from bs4 import BeautifulSoup
from NetConnect import getWebElement,getWebFile
import re

elements=getWebElement("http://www.bilibili.com")
print(elements.html.meta)
