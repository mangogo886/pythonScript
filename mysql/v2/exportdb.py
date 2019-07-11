#!/usr/bin/env python
#coding:utf-8
#用于私有云部署批量部署数据库

import os
import MySQLdb


host = ''
user = ''
passwd = ''
empty = '/data/ops/script/exportdb/db1'
notempty='/data/ops/script/exportdb/db2'

f1=open(empty,'r')
f2=open(notempty,'r')

for i1 in f1.readlines():
    ename = i1.strip()
    os.system("/usr/bin/mysqldump -h %s -u%s -p%s -d %s >%s.dump"%(host,user,passwd,ename,ename))
    print ename+" exported-----notdata"

for i2 in f2.readlines():
    dname = i2.strip()
    os.system("/usr/bin/mysqldump -h %s -u%s -p%s  %s>%s.dump"%(host,user,passwd,dname,dname))
    print dname+" exported"