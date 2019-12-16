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
    back="/data/ops/script/zk"
    os.system("/usr/bin/mysqldump -h   -uopszk -pzk89536 %s >%s/qky_ops%s.dump"%(database,back,date))
    
    con=MySQLdb.connect(host='',user='opszk',passwd='zk89536',db='qky_ops',charset="utf8")
    cursor=con.cursor()
    delsql="delete  FROM cm_zk_node  where zk_id=1001 and path like '/configs/qky%';"
    cursor.execute(delsql)
    con.commit() 

    zk_hosts=""
    
    zk=KazooClient(zk_hosts)
    zk.start()

    zknod="/configs/qky"

    children=zk.get_children(zknod)
    for chil in children:
        two=zknod+"/"+chil
        children2=zk.get_children(two)
        for chil2 in children2:
            three=two+"/"+chil2
            children3=zk.get_children(three)
            for chil3 in children3:
                four=three+"/"+chil3
                data,stat=zk.get(four)
                insertsql="INSERT INTO qky_ops.cm_zk_node(`app_code`, `path`, `content`, `zk_id`, `is_sync`, `deleted`, `update_user`) VALUES ( '%s', '%s', '%s', '1001', 0, 0,'zhumin');"%(chil,four,data)
                cursor.execute(insertsql)
                con.commit()
    delsql2="delete  FROM cm_zk_node where content='None' and zk_id=1001;" 
    cursor.execute(delsql2)
    con.commit() 

    cursor.close()
    con.close()

    zk.stop()
readzk()