#!/usr/bin/env python
#coding:utf8

import socket
import time
import random
import MySQLdb
import os
from kazoo.client import *

def sys_zk():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    while True:
        time.sleep(seconds)
        send_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        con=MySQLdb.connect(host=ip,user=user,passwd=passwd,db=db,charset="utf8")
        cursor=con.cursor()
        sql="select count(*) from zk_node where mark=0;"
        cursor.execute(sql)
        mark_list=cursor.fetchall()
        con.commit()
        if mark_list[0][0]==0:
            print "%s-----无更新记录-----"%send_time
        else:
            print "%s-----%s 条更新记录，开始插入zk...."%(send_time,mark_list[0][0])
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
                print node[0],node[1],"%s-----插入配置到%s"%(send_time,zk_hosts)
                update_sql='update zk_node set mark=1 where path="%s";'%node[0]
                cursor.execute(update_sql)
                con.commit()
            print "%s-----更新配置完成，总共更新记录%s 条"%(send_time,mark_list[0][0])
            zk.stop()
        cursor.close()
        con.close()

if __name__ == "__main__":
    host='127.0.0.1'
    port=9899
    seconds = random.randint(3, 5)
    zk_hosts = "172.17.1.24:2181"
    ip = '172.17.1.24'
    user = 'admin'
    passwd = 'Qky2##2019'
    db = 'qky_ops'
    sys_zk()