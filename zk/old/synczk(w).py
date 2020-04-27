#!/usr/bin/env python 
#coding:utf-8
#批量插入zk节点数据

import MySQLdb
import os
from kazoo.client import *

zk_hosts="ip:2181"
zk=KazooClient(zk_hosts)
zk.start()

con=MySQLdb.connect(host='',user='root',passwd='',db='qky_ops',charset="utf8")
cursor=con.cursor()
sql="select path,content from zk_node"
cursor.execute(sql)
result=cursor.fetchall()
for t in result:
    key=t[0].encode('utf8')
    nu=t[1].encode('utf8')
    if zk.exists(key):

        zk.set(key,nu)
    else:
        zk.ensure_path(key)
        zk.set(key,nu)
cursor.close()
con.close()
zk.stop()