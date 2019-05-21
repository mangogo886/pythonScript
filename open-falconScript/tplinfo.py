#!/usr/bin/env python
#coding:utf-8
#配置监控模板，模板需要先创建好


import ConfigParser
import MySQLdb
import os

configPath="config.ini"
cf=ConfigParser.ConfigParser()
cf.read(configPath)
section = cf.sections()

con=MySQLdb.connect(host="10.137.215.45",user="openFalcon",passwd="Daef=596",db="falcon_portal",charset="utf8")
cursor=con.cursor()

for grpName in section:
    #添加模板监控信息
    selectTpl='select tpl.id from tpl where tpl_name="%s";'%grpName
    cursor.execute(selectTpl)
    TplId=cursor.fetchone()
    opts=cf.get(grpName,'app')
    tomcatList=opts.split(',')
    for tomcat in tomcatList:
        tomcatName="cmdline="+tomcat
            
        insertStrategy='INSERT INTO `falcon_portal`.`strategy`( `metric`, `tags`, `max_step`, `priority`, `func`, `op`, `right_value`,  `tpl_id`) VALUES ( "proc.num", "%s", 10, 0, "all(#3)", "!=", "1", "%s");'%(tomcatName,TplId[0])
        cursor.execute(insertStrategy)
        con.commit()
        print "成功添加进程 %s 到模板 %s"%(tomcat,grpName)

cursor.close()
con.close()