#!/usr/bin/env python
#coding:utf-8
#用于创建模板和主机组，并绑定关系，只适合主机组名称和模板名称相同的情况


import ConfigParser
import MySQLdb
import os

configPath="config.ini"
cf=ConfigParser.ConfigParser()
cf.read(configPath)
section = cf.sections()

con=MySQLdb.connect(host="",user="openFalcon",passwd="Daef=596",db="falcon_portal",charset="utf8")
cursor=con.cursor()


for grpName in section:
    #创建主机组
    insertGrp='INSERT INTO `falcon_portal`.`grp`( `grp_name`, `create_user`, `come_from`) VALUES ("%s", "root",1);'%grpName
    cursor.execute(insertGrp)
    con.commit()

    print "创建主机组 %s 成功............."%grpName

    #获取新创建的主机组id
    selectgrp='SELECT grp.id FROM `grp` where grp_name="%s"'%grpName
    cursor.execute(selectgrp)
    grpId=cursor.fetchone() 

    #获取需要关联主机组的主机id

    hostName=grpName    #用主机名创建主机组。所以这里相等
    selecthost='select host.id from host where hostname="%s"'%hostName
    cursor.execute(selecthost)
    hostId=cursor.fetchone()

    #关联主机组和主机
    insertGrpHost='INSERT INTO `grp_host`(`grp_id`, `host_id`) VALUES ("%s", "%s");'%(grpId[0],hostId[0])
    cursor.execute(insertGrpHost)
    con.commit()
    print "关联主机组 %s 和主机 %s........."%(grpId[0],hostId[0])

    #构造告警发送人id
    selectActionId='SELECT action.id FROM `action`   order by id desc limit 1'
    cursor.execute(selectActionId)
    tempId=cursor.fetchone()
    actionId=tempId[0]+1
    insertAction='INSERT INTO `falcon_portal`.`action`(`id`, `uic`) VALUES ("%s", "ops");'%(actionId)
    cursor.execute(insertAction)
    con.commit()

    #创建模板
    insertTpl='INSERT INTO `falcon_portal`.`tpl`( `tpl_name`, `action_id`,`create_user`) VALUES ("%s","%s","root");'%(grpName,actionId)
    cursor.execute(insertTpl)
    con.commit()

    print "创建模板 %s 成功......"%grpName

    #提取新建模板id
    selectTpl='select tpl.id from tpl where tpl_name="%s";'%grpName
    cursor.execute(selectTpl)
    TplId=cursor.fetchone()

    #绑定主机组和模板
    insertGrp_Tpl='INSERT INTO `falcon_portal`.`grp_tpl`(`grp_id`, `tpl_id`, `bind_user`) VALUES (%s, %s, "root");'%(grpId[0],TplId[0])
    cursor.execute(insertGrp_Tpl)
    con.commit()

    print "绑定主机组 %s 和模板 %s 成功"%(grpId[0],TplId[0])


cursor.close()
con.close()