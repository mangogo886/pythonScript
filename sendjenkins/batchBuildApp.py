#!/usr/bin/env python
#coding:utf-8

import urllib2
import json
import sys
import jenkins
import time
import ConfigParser
reload(sys)
sys.setdefaultencoding( "utf-8" )


def buildjob():
    envlist=deployenv.split(",")
    cf = ConfigParser.ConfigParser()
    cf.read(confurl)
    for list in envlist:
        jkurl = cf.get(list, 'url')

        try:
            server = jenkins.Jenkins(jkurl, username=user, password=passwd)
            if server.job_exists(name=jobName):
                jobinfo = server.get_job_info(jobName)
                if jobinfo['actions'][0]:
                    server.build_job(jobName,parameters=param_dict)
                    lastBuildNumber = server.get_job_info(jobName)['lastBuild']['number']
                    buil = server.get_build_info(jobName, lastBuildNumber)['building']
                    # 判断是否正在构建
                    print list,jobName,"开始构建....."
                    while buil:
                        time.sleep(1)
                        buil = server.get_build_info(jobName, lastBuildNumber)['building']

                    console = server.get_build_console_output(jobName, lastBuildNumber)
                    print console
                else:
                    print list, jobName, "无参数构建"
                    server.build_job(jobName)
                    lastBuildNumber = server.get_job_info(jobName)['lastBuild']['number']
                    buil = server.get_build_info(jobName, lastBuildNumber)['building']
                    # 判断是否正在构建
                    print list, jobName, "开始构建....."
                    while buil:
                        time.sleep(1)
                        buil = server.get_build_info(jobName, lastBuildNumber)['building']

                    console = server.get_build_console_output(jobName, lastBuildNumber)
                    print console
                print list,jobName,"存在"
            else:
                print list,jobName, "不存在"
        except Exception, e:
            print list,jkurl,"无法登录"

if __name__=='__main__':
    user = ""
    passwd = ""
    # 构建环境参数
    deployenv = sys.argv[1]
    # 构建应用参数
    jobName = sys.argv[2]
    # 构建版本号
    version = sys.argv[3]
    confurl = "urls.ini"
    param_dict = {"commit_version": version}
    buildjob()

