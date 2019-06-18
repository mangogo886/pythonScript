#!/usr/bin/env python
#coding:utf-8
#批量导出mysql数据库


import os

def exdb(databases):
    for database in databases:
        dbName=database+".dump"
        back=os.path.join(path,dbName)
        os.system("/usr/bin/mysqldump -h 127.0.0.1 -uroot -p123456 %s >%s"%(database,back))
        print database+" 导出数据文件 "+back 



if __name__ == "__main__":
    databases=['qky_cgyy','qky_clgl','qky_dorm','qky_rsda']
    path="/data/database/dabases/back"
    exdb(databases)