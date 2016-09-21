#coding:utf8 
from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

def getWebElement(url):
    try:
        html = urlopen(url)
    except(HTTPError,URLError):
        print("Outcome a Http/Url Error")
        return None
    try:
        elements = BeautifulSoup(html,"html.parser")
    except AttributeError:
        print("Html file has something wrong!")
    else:
        return elements

def getWebFile(localurl):

    try:
        with open('pixiv.htm','r',encoding='utf-8') as netfile:
            elements = BeautifulSoup(netfile,"html.parser",from_encoding='utf-8',exclude_encodings='gbk')
            return elements
    except IOError:
        print("Fales in opening file")
    
def readdict(dict):
    for key,value in dict.items():
        print("\nKey: " + key)
        print("Value: " + value);
