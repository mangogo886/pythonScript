#!/usr/bin/env python
#coding:utf-8
#读取zk节点数据

import MySQLdb
import os
from kazoo.client import *
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def readzk():
    date=time.strftime('%Y%m%d',time.localtime())
    database="qky_ops"
    con=MySQLdb.connect(host='10.10.200.11',user='admin',passwd='',db='qky_ops',charset="utf8")
    cursor=con.cursor()
    delesql="delete from qky_ops.zk_node"
    cursor.execute(delesql)
    con.commit()
    zk_hosts="10.10.200.11:2181"
    
    zk=KazooClient(zk_hosts)
    zk.start()

    zknod1="/configs/qky"
    zknod2="/startconfigs/qky"
    children=zk.get_children(zknod1)
    childrens=zk.get_children(zknod2)
    for chil in children:
        chil2=os.path.join(zknod1,chil)
        if zk.exists(chil2):
            children2=zk.get_children(chil2)
            for chil in children2:
                chil3=os.path.join(chil2,chil)
                if zk.exists(chil3):
                    children3=zk.get_children(chil3)
                    for chil in children3:
                        chil4=os.path.join(chil3,chil)
                        data,stat=zk.get(chil4)
                        updatsql="INSERT INTO qky_ops.zk_node values('%s','%s');"%(chil4,data)
                        cursor.execute(updatsql)
                        con.commit()
    for chil21 in childrens:
        chil22=os.path.join(zknod2,chil21)
        if zk.exists(chil22):
            childrens2=zk.get_children(chil22)
            for chil23 in childrens2:
                chil24=os.path.join(chil22,chil23)
                data1,stat=zk.get(chil24)
                updatsql1="INSERT INTO qky_ops.zk_node values('%s','%s');"%(chil24,data1)
                cursor.execute(updatsql1)
                con.commit()

    cursor.close()
    con.close()
    
    zk.stop()
    print "读取完成......"
readzk()