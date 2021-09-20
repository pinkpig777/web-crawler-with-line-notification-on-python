# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 16:12:36 2021

@author: charl
"""
import sys
import re
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def readData():
    with open(r'YOUR PATH','r',encoding = 'utf-8') as fh :
        url = fh.readline()
    return url

def autoCheck(url):
    driver = webdriver.Chrome(r'YOUR PATHchromedriver.exe')
    driver.get(url)
    try : 
        next_page = driver.find_element_by_id('read_next')
        next_page.click()
        time.sleep(1)
        url = driver.current_url
        print("check for new chapter success ")
        driver.close()
        return url
    except :
        driver.close()
        print("this page is the newest one.")
        sys.exit(1)

def textParsing(url):
    try :
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf-8'
        print("requests success")
    except:
        print('fail to connect to web')
        sys.exit(2)
    soup = BeautifulSoup(r.text,'html.parser')
    dic = {'class':'rp-article bookContent uu_cont'}
    element = soup.find_all('div',dic)
    title = soup.title.string
    tmp = str(element)
    tmp_2 = re.split(r'\s+|<.*?>',tmp)
    abandon ={"window.adsbygoogle","||","[]).push({})",'','(adsbygoogle','=','[]).push({});','[',']'}
    read =[title]+[i for i in tmp_2 if i not in abandon]
    count = 0
    with open(r"YOUR PATH.book.txt",'w',encoding = 'utf-8') as fh:
        fh.write(url+'\n')
        for sentence in read:
            fh.write(sentence + '\n')
            count +=1
            print("\rcurrent progress :{:.2f}%".format(count*100/len(read)),end= '',flush = True)


def main():
    url = readData()
    new_url = autoCheck(url)
    textParsing(new_url)
 
    
