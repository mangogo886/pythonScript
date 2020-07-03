#!/usr/bin/env python
#coding:utf-8

import jenkins
import os
import sys
import time
import threading
reload(sys)
sys.setdefaultencoding( "utf-8" )



def svnhw():
    jenkins_url="http://jk.qky.cnn/"

    server=jenkins.Jenkins(jenkins_url,username=user_id,password=api_token)
    server.build_job(job_name,parameters=param_dict)
    queue_job=server.get_queue_info()
    while queue_job[0]['task']['name']==job_name:
        print job_name,"正处于pending 队列，请等待"
        time.sleep(10)
        break
    lastBuildNumber = server.get_job_info(job_name)['lastBuild']['number']
    console=server.get_build_console_output(job_name,lastBuildNumber)
    print "华为云job最新构建序号：",lastBuildNumber
    print "华为云job--构建日志：",console


if __name__=='__main__':
    user_id = "yuanhao"
    api_token = "Frg*5796"
    job_name = 'add-ip-svn-36902'
    version=sys.argv[1]
    param_dict = {"ip": version}
    svnhw()
~