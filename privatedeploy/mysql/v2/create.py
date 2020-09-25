#!/usr/bin/env python
#coding:utf-8
#用于私有云部署批量创建数据库

import os
import MySQLdb

host = '127.0.0.1'
user = 'root'
passwd = '123456'
path = 'dbname'
con = MySQLdb.connect(host=host, user=user, passwd=passwd, charset="utf8")
cursor = con.cursor()


f=open(path,'r')
for i in f.readlines():
    name=i.strip()
    try:
        sql = "create database %s default character set  utf8 collate utf8_general_ci;" % name
        cursor.execute(sql)
        print name + " successfull created"
    except Exception, e:
        print name + " exit,not created"

cursor.close()
con.close()

