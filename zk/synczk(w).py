#!/usr/bin/env python
#coding:utf-8
#批量同步zk

import MySQLdb
import os
from kazoo.client import *

def sys_zk():
    con=MySQLdb.connect(host=ip,user=user,passwd=passwd,db=db,charset="utf8")
    cursor=con.cursor()
    sql="select count(*) from zk_node where mark=0;"
    cursor.execute(sql)
    mark_list=cursor.fetchall()
    con.commit()
    if mark_list[0][0]==0:
        print "无更新记录"
    else:
        print "%s 条更新记录，开始插入zk...."%mark_list[0][0]
        sqlpath="select path,content from zk_node where mark=0;"
        cursor.execute(sqlpath)
        path_list = cursor.fetchall()
        zk = KazooClient(zk_hosts)
        zk.start()
        for node in path_list:
            key = node[0].encode('utf8')
            context = node[1].encode('utf8')
            zk.ensure_path(key)
            zk.set(key,context)
            print node[0],node[1],"插入配置到%s"%zk_hosts
            update_sql='update zk_node set mark=1 where path="%s";'%node[0]
            cursor.execute(update_sql)
            con.commit()
        print "更新配置完成，总共更新记录%s 条"%mark_list[0][0]
    cursor.close()
    con.close()

if __name__=="__main__":
    zk_hosts = "10.136.56.27:2181"
    ip = '127.0.0.1'
    user = 'root'
    passwd = '123456'
    db = 'qky_ops'
    sys_zk()