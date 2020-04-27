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
    #date=time.strftime('%Y%m%d',time.localtime())
    database="qky_ops"
    con=MySQLdb.connect(host='10.10.200.11',user='admin',passwd='',db='qky_ops',charset="utf8")
    cursor=con.cursor()
    delesql="delete from qky_ops.zk_node where path like '/configs%' or path like '/startconfigs%'"
    cursor.execute(delesql)
    con.commit()
    zk_hosts="10.10.200.11:2181"
    
    zk=KazooClient(zk_hosts)
    zk.start()

    dynamic="/configs"
    startconfig="/startconfigs"
    dynodes=zk.get_children(dynamic)
    stnodes=zk.get_children(startconfig)

    #获取启动配置节点
    if len(stnodes)!=0:
        for stnode in stnodes:
            stnode=os.path.join(startconfig,stnode)
            secondestnodes=zk.get_children(stnode)
            if len(secondestnodes)!=0:
                for secondestnode in secondestnodes:
                    thirdnodes=os.path.join(stnode,secondestnode)
                    fourthnodes=zk.get_children(thirdnodes)
                    if len(fourthnodes)!=0:
                        for fourthnode in fourthnodes:
                            lastnode=os.path.join(thirdnodes,fourthnode)
                            data2,stat=zk.get(lastnode)
                            insertsql2="INSERT INTO qky_ops.zk_node(appCode,path,content) values('%s','%s','%s');"%(secondestnode,lastnode,data2)
                            cursor.execute(insertsql2)
                            con.commit()
                            
    else:
        print "null"

    #获取动态配置节点
    if len(dynodes)!=0:
        for dynode in dynodes:
            dynode=os.path.join(dynamic,dynode)
            secondestdynodes=zk.get_children(dynode)
            if len(secondestdynodes)!=0:
                for secondestdynodena in secondestdynodes:
                    thirddynodes=os.path.join(dynode,secondestdynodena)
                    fourthdynodes=zk.get_children(thirddynodes)
                    if len(fourthdynodes)!=0:
                        for fourthdynode in fourthdynodes:
                            fifthdyndodes=os.path.join(thirddynodes,fourthdynode)
                            sixthdynodes=zk.get_children(fifthdyndodes)
                            if len(sixthdynodes)!=0:
                                for sixthdynode in sixthdynodes:
                                    seventhdynodes=os.path.join(fifthdyndodes,sixthdynode)
                                    data1,stat1=zk.get(seventhdynodes)
                                    insertsql1="INSERT INTO qky_ops.zk_node(appCode,path,content) values('%s','%s','%s');"%(secondestdynodena,seventhdynodes,data1)
                                    cursor.execute(insertsql1)
                                    con.commit()
                            else:
                                data,stat=zk.get(fifthdyndodes)
                                insertsql="INSERT INTO qky_ops.zk_node(appCode,path,content) values('%s','%s','%s');"%(secondestdynodena,fifthdyndodes,data)
                                cursor.execute(insertsql)
                                con.commit()
    zk.stop()
    cursor.close()
    con.close()
    print "读取完成......"
readzk()