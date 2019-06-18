#!/usr/bin/env python
#coding:utf-8
#批量导入mysql数据库


import os

def fileList(path):
    for dirs,listdir,files in os.walk(path):
        for fileName in files:
            database=fileName[:-5]
            databaseFile=os.path.join(path,fileName)
            os.system("/usr/bin/mysql -h 127.0.0.1 -uroot -p123456 %s <%s"%(database,databaseFile))
            print database+" 导入数据文件 "+databaseFile


if __name__ == "__main__":
    path="/data/database/dabases"
    fileList(path)