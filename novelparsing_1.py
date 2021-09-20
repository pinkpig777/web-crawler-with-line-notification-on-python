# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 13:02:42 2021

@author: charl
"""
import requests
from bs4 import BeautifulSoup
import re
r = requests.get('https://t.uukanshu.com/read.aspx?tid=128714&sid=76399')
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text,'html.parser')
dic = {'class':'rp-article bookContent uu_cont'}
element = soup.find_all('div',dic)
title = soup.title.string
tmp = str(element)
tmp_2 = re.split(r'\s+|<.*?>',tmp)
abandon ={"window.adsbygoogle","||","[]).push({})",'','(adsbygoogle','=','[]).push({});','[',']'}
read =[title]+[i for i in tmp_2 if i not in abandon]
with open(r"C:\Users\charl\OneDrive\桌面\python\爬蟲\book.txt",'w',encoding = 'utf-8') as fh:
    for sentence in read:
        fh.write(sentence + '\n')
