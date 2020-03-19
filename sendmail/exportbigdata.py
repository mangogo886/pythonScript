#!/usr/bin/env python
#coding:utf8
#导出数据库并写入excel

import MySQLdb
import os
import xlwt
import time


filedir='/data/ops/script/sendmai/'
name=time.strftime('%Y%m%d',time.localtime())
file =filedir+name+".xls"

con=MySQLdb.connect(host='',user='',passwd='',db='',charset="utf8")

cursor=con.cursor()

sql=""

cursor.execute(sql)

fileds = cursor.description  #获取数据库字段
result=cursor.fetchall()

wbk = xlwt.Workbook()
sheet1 = wbk.add_sheet('sheet1',cell_overwrite_ok=True)

#写入字段到excel
for filed in range(0,len(fileds)):
    sheet1.write(0,filed,fileds[filed][0])
    
#写入数据到excel    
for row in range(1,len(result)+1):
    for col in range(0,len(fileds)):
        sheet1.write(row,col,result[row-1][col])

wbk.save(file)


cursor.close()
con.close()