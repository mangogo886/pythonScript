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


def envname(list):
    if list=="hw":
        name="华为云"
    elif list=="nsfz":
        name="南师附中"
    elif list=="xxzx":
        name="湘西中学"
    elif list=="xxxx":
        name="湘西小学"
    elif list=="xxyey":
        name="湘西幼儿园"

    elif list=="gm":
        name="高密中学"
    elif list=="gm":
        name="高密中学"
    elif list=="rq":
        name="瑞泉中学"
    elif list=="wnzx":
        name="渭南中学"
    elif list=="hsxx":
        name="护士学校"
    elif list=="snzx":
        name="思南中学"

    elif list=="zsys":
        name="中山一中"
    elif list=="gzjl":
        name="广州金隆"
    elif list=="sdlj":
        name="顺德九江"
    elif list=="xa30":
        name="西安30中"
    else:
        name="没有匹配名字"    

    return name

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
                    # 设置输出字体蓝色
                    print ("\033[1;34m %s %s 构建成功..... \033[0m"%(listname,jobName))
            else:
                print("\033[1;31m %s %s 不存在\033[0m"%(listname,jobName))
        except Exception, e:
            #设置输出字体红色
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
    confurl = "/data/ops/scripts/sendjkbuild/batchBuildApp/urls.ini"
    param_dict = {"commit_version": version}
    buildjob()