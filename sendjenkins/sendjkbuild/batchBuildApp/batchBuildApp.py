#!/usr/bin/env python
#coding:utf-8

import urllib2
import json
import sys
import jenkins
import time
import ConfigParser
sys.path.append("/data/ops/scripts/sendjkbuild")
from common.chinaName import * 
reload(sys)
sys.setdefaultencoding( "utf-8" )


def buildjob():
    envlist=deployenv.split(",")
    cf = ConfigParser.ConfigParser()
    cf.read(confurl)
    for list in envlist:
        listname=envname(list)
        jkurl = cf.get(list, 'url')
        try:
            server = jenkins.Jenkins(jkurl, username=user, password=passwd,timeout =20)
            if server.job_exists(name=jobName):
                jobinfo = server.get_job_info(jobName)
                if jobinfo['actions'][0]:
                    print ("\033[1;34m %s %s 开始构建..... \033[0m"%(listname,jobName))
                    server.build_job(jobName,parameters=param_dict)
                    queue_job=server.get_queue_info()
                    while queue_job:
                        queue_job=server.get_queue_info()
                        for queue_building_job in queue_job:
                            queue_name=queue_building_job['task']['name']
                            if queue_name!=jobName:
                                break

                    lastBuildNumber = server.get_job_info(jobName)['lastBuild']['number']
                    buil = server.get_build_info(jobName, lastBuildNumber)['building']
                    while buil:
                            time.sleep(1)
                            buil = server.get_build_info(jobName, lastBuildNumber)['building']
                          
                    console = server.get_build_console_output(jobName, lastBuildNumber)
                    lastBuildResult=server.get_build_info(jobName,lastBuildNumber)['result']
                    print ("\033[1;34m %s 构建序号：%s..... \033[0m"%(listname,lastBuildNumber))
                    print console
                    #print ("\033[1;34m %s %s 构建结果: %s..... \033[0m"%(listname,jobName,lastBuildResult))
                    if lastBuildResult=="SUCCESS":
                        print ("\033[1;34m %s %s 构建成功..... \033[0m"%(listname,jobName))
                    else:
                        print("\033[1;31m %s %s  构建失败.....\033[0m"%(listname,jobName))
           
                else:
                    print("\033[1;31m %s %s 构建失败,没有设置构建参数version,请到对应环境修改后再重新执行.....\033[0m"%(listname,jobName))
                 
            else:
                print("\033[1;31m %s %s 不存在\033[0m"%(listname,jobName))  
        except Exception, e:
            print("\033[1;31m %s %s 登录失败.....\033[0m"%(listname,jkurl)) 
 
if __name__=='__main__':
    user = "qtqky"
    passwd = "Ghyfv#%5896"
    # 构建环境参数
    deployenv = sys.argv[1]
    # 构建应用参数
    jobName = sys.argv[2]
    # 构建版本号
    version = sys.argv[3]
    confurl = "/data/ops/scripts/sendjkbuild/common/urls.ini"
    param_dict = {"version": version}
    buildjob()