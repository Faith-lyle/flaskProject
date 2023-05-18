#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
@Name: flaskProject>>demo.py
@Auth: long.hou
@Email: long.hou2@luxshare-ict.com
@Date: 2023/5/18-11:06
@IDE: PyCharm 
"""
import requests

# ssion = requests.session()
#
url = 'http://10.103.3.178/webroot/decision/login?origin=88e26597-3ee0-42ea-a9ef-1728f215bfde'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
#
# r = requests.get(url=url,headers=headers)
# print(r.text)

s = requests.session()
# 设置cookie
cookie_dict = {"last_login_info": "true",
               'fine_auth_token': 'eyJhbGciOiJIUzI1NiJ9'
                                  '.eyJpc3MiOiJmYW5ydWFuIiwiaWF0IjoxNjg0MzgwMzU5LCJleHAiOjE2ODQ0MzQzMDUsInN1YiI6IjE2MDgzNzI4IiwiZGVzY3JpcHRpb24iOiJbNGZhZl1bOWY5OV0oMTYwODM3MjgpIiwianRpIjoiL1NaeGNTZDJWVWtYbnpPeGpCQjkvbit6NlZDWkpkR1Zwc0M2RkZuUmJ6dmlMTGxSIn0.h-8u2IMDGEq6-eVZWyz5a_E7PdeMh5-pZW8p64Sv6MQ',
               'fine_remember_login': "-1"}
cookies = requests.models.cookiejar_from_dict(cookie_dict, cookiejar=None, overwrite=True)
s.cookies = cookies
for i in range(3):
    r = s.get('http://10.103.3.178/webroot/decision/view/form?op=chartauto&cmd=chart_auto_refresh&chartID=chart8_c_c_c_c_c_c_c_c__de864f16-1ddc-4f1e-beec-7cf073507769__index__0&chartWidth=35&chartHeight=112&sheetIndex=0&ecName=&__time=1684380673814')
    print(r.headers)
