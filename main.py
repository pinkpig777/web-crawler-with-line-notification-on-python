# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 11:30:26 2021

@author: charl
"""
from automatic_novel_getter import *
main()
from line_noify import lineNotifyMessage
text = []
with open(r'C:\Users\charl\OneDrive\桌面\python\web_crawler\book.txt','r',encoding = 'utf-8') as fh :
    url = fh.readline()
msg = url 
token = 'SQGU8rhDkJ7FLiw63YZwq5KxR42HssydjR32uV6THou'
lineNotifyMessage(token,msg)
