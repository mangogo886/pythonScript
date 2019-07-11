#!/usr/bin/env python
#coding:utf-8
#用于私有云部署批量部署数据库

import os
import MySQLdb


host = ''
user = ''
passwd = ''
path = 'dbname'

f=open(path,'r')

for i in f.readlines():
    name = i.strip()
    os.system("/usr/bin/mysql -h %s -u%s -p%s %s <%s.dump"%(host,user,passwd,name,name))
    print ename+" imported"

