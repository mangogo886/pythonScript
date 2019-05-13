#!/usr/bin/env python
#coding:utf-8

import re
import os



a=":"
proxy=raw_input("entry ip:port: ")
file=raw_input("entry nginxfile: ")
f=open("txt",'r')
str=f.read()


# 分为开头，中间和结尾三部分，提取可能包含ip地址的字符串
# 匹配中间部分的ip，返回列表
result = re.findall(r'\D(?:\d{1,3}\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\D',str)

# 匹配开头可能出现ip
ret_start = re.match(r'(\d{1,3}\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\D',str)
if ret_start:
    result.append(ret_start.group())

# 匹配结尾
ret_end = re.search(r'\D(\d{1,3}\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$',str)
if ret_end:
    result.append(ret_end.group())


# 构造列表保存ip地址
ip_list = []
for r in result:
    # 正则提取ip
    ret = re.search(r'((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)', r)
    if ret:
        # 匹配成功则将ip地址添加到列表中
        ip_list.append(ret.group())

port=re.findall("[0-9][0-9][0-9][0-9]",str)
for i in port:
    info=ip_list[0]+a+i
    os.system("sed -i 's/%s/%s/g' %s"%(info,proxy,file))

# 输入结果列表d
#print ip_list[0]