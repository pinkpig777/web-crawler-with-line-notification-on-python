# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 11:02:58 2021

@author: charl
"""
import requests

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
	
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code
	
message = ''
token = 'SQGU8rhDkJ7FLiw63YZwq5KxR42HssydjR32uV6THou'
lineNotifyMessage(token, message)
