#!/usr/bin/env python
#coding:utf-8

import urllib2
import json
import sys
import jenkins
import time
import ConfigParser
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
        apiToken = cf.has_option(list, 'api_token')
        if apiToken:
            apiToken = cf.get(list, 'api_token')
            try:
                server = jenkins.Jenkins(jkurl, username=user, password=apiToken, timeout=20)
                if server.job_exists(name=jobName):
                    jobinfo = server.get_job_info(jobName)
                    if jobinfo['actions'][0]:
                        server.build_job(jobName, parameters=param_dict)
                        lastBuildNumber = server.get_job_info(jobName)['lastBuild']['number']
                        buil = server.get_build_info(jobName, lastBuildNumber)['building']
                        # 判断是否正在构建
                        print ("\033[1;34m %s %s 开始构建..... \033[0m" % (listname, jobName))
                        while buil:
                            time.sleep(1)
                            buil = server.get_build_info(jobName, lastBuildNumber)['building']

                        console = server.get_build_console_output(jobName, lastBuildNumber)
                        print console
                        print ("\033[1;34m %s %s 构建成功..... \033[0m" % (listname, jobName))
                    else:
                        print ("\033[1;34m %s %s 无参数构建.... \033[0m" % (listname, jobName))
                        server.build_job(jobName)
                        lastBuildNumber = server.get_job_info(jobName)['lastBuild']['number']
                        buil = server.get_build_info(jobName, lastBuildNumber)['building']
                        # 判断是否正在构建
                        print ("\033[1;34m %s %s 开始构建..... \033[0m" % (listname, jobName))
                        while buil:
                            time.sleep(1)
                            buil = server.get_build_info(jobName, lastBuildNumber)['building']

                        console = server.get_build_console_output(jobName, lastBuildNumber)
                        print console
                        print ("\033[1;34m %s %s 构建成功..... \033[0m" % (listname, jobName))
                else:
                    print("\033[1;31m %s %s 不存在\033[0m" % (listname, jobName))
            except Exception, e:
                print("\033[1;31m %s %s 登录失败.....\033[0m" % (listname, jkurl))

        else:
            print apiToken
            try:
                server = jenkins.Jenkins(jkurl, username=user, password=passwd,timeout =20)
                if server.job_exists(name=jobName):
                    jobinfo = server.get_job_info(jobName)
                    if jobinfo['actions'][0]:
                        server.build_job(jobName,parameters=param_dict)
                        lastBuildNumber = server.get_job_info(jobName)['lastBuild']['number']
                        buil = server.get_build_info(jobName, lastBuildNumber)['building']
                        # 判断是否正在构建
                        print ("\033[1;34m %s %s 开始构建..... \033[0m"%(listname,jobName))
                        while buil:
                            time.sleep(1)
                            buil = server.get_build_info(jobName, lastBuildNumber)['building']

                        console = server.get_build_console_output(jobName, lastBuildNumber)
                        print console
                        print ("\033[1;34m %s %s 构建成功..... \033[0m"%(listname,jobName))
                    else:
                        print ("\033[1;34m %s %s 无参数构建.... \033[0m"%(listname,jobName))
                        server.build_job(jobName)
                        lastBuildNumber = server.get_job_info(jobName)['lastBuild']['number']
                        buil = server.get_build_info(jobName, lastBuildNumber)['building']
                        # 判断是否正在构建
                        print ("\033[1;34m %s %s 开始构建..... \033[0m"%(listname,jobName))
                        while buil:
                            time.sleep(1)
                            buil = server.get_build_info(jobName, lastBuildNumber)['building']

                        console = server.get_build_console_output(jobName, lastBuildNumber)
                        print console
                        print ("\033[1;34m %s %s 构建成功..... \033[0m"%(listname,jobName))
                else:
                    print("\033[1;31m %s %s 不存在\033[0m"%(listname,jobName))
            except Exception, e:
                print("\033[1;31m %s %s 登录失败.....\033[0m"%(listname,jkurl))

if __name__=='__main__':
    user = ""
    passwd = ""
    # 构建环境参数
    deployenv = sys.argv[1]
    # 构建应用参数
    jobName = "qky-oa-v2-frontend"
    # 构建版本号
    version = sys.argv[2]
    confurl = "/data/ops/scripts/sendjkbuild/common/urls.ini"
    param_dict = {"commit_version": version}
    buildjob()
