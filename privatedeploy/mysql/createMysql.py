#!/usr/bin/env python
#coding:utf-8
#用于批量创建数据库创建数据库

import os
import MySQLdb

host='127.0.0.1'
user='root'
passwd='123456'
path='/data/mysqlTest/db'
databases=[]

con=MySQLdb.connect(host=host,user=user,passwd=passwd,charset="utf8")
cursor=con.cursor()

for dirs,listdir,files in os.walk(path):
    for fileName in files:
        dbname=fileName[:-5]
        databases.append(dbname)


def create(databases):
    for database in databases:
        try:

            sql="create database %s default character set  utf8 collate utf8_general_ci;"%database
            cursor.execute(sql)
            print database+" successfull created"
        except Exception,e:
            print database+" exit,not created"
    cursor.close()
    con.close()
create(databases)