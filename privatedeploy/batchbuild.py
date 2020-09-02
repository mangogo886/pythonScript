#!/usr/bin/env python
#coding:utf-8
#私有化部署，批量执行build


import urllib2
import json
import sys
import jenkins
import time
import ConfigParser
import time



#执行批量构G建函数
def buildjob():
    cf=ConfigParser.ConfigParser()
    cf.read(configPath)
    hostlist=cf.sections()
    server = jenkins.Jenkins(jkurl, username=user, password=passd)
    for host in hostlist:
        applist=cf.get(host,'app').split(',')
        for ap in applist:
            fejob=ap+fesuffix
            h5job=ap+h5suffix
            rpcjob=ap+rpcsuffix
            bejob=ap+besuffix

            #构建前端
            if server.job_exists(fejob):
                jobarg=server.get_job_info(fejob)
                if jobarg['actions'][0]:
                    print fejob,"开始构建"
                    server.build_job(fejob,parameters=param_dict)
                else:
                    print fejob,"开始构建"
                    print fejob,"无参数构建"    
                    server.build_job(fejob)
            #构建h5端
            if server.job_exists(h5job):
                jobarg=server.get_job_info(h5job)
                if jobarg['actions'][0]:
                    print h5job,"开始构建"
                    server.build_job(h5job,parameters=param_dict)
                else:
                    print h5job,"开始构建"    
                    print h5job,"无参数构建"
                    server.build_job(h5job)
            #构建RPC
            if server.job_exists(rpcjob):
                jobarg=server.get_job_info(rpcjob)
                if jobarg['actions'][0]:
                    print rpcjob,"开始构建"
                    server.build_job(rpcjob,parameters=param_dict)
                else:
                    print rpcjob,"开始构建"
                    print rpcjob,"无参数构建"
                    server.build_job(rpcjob)
            #构建后端
            if server.job_exists(bejob):
                jobarg=server.get_job_info(bejob)
                if jobarg['actions'][0]:
                    print bejob,"开始构建"
                    server.build_job(bejob,parameters=param_dict)
                else:
                    print bejob,"开始构建"
                    print bejob,"无参数构建"
                    server.build_job(bejob)


#获取批量构建后的结果,默认不执行。按需在入口启用
def getBuildResult():

    cf=ConfigParser.ConfigParser()
    cf.read(configPath)
    hostlist=cf.sections()
    server = jenkins.Jenkins(jkurl, username=user, password=passd)


    for host in hostlist:
        applist=cf.get(host,'app').split(',')
        for ap in applist:
            fejob=ap+fesuffix
            h5job=ap+h5suffix
            rpcjob=ap+rpcsuffix
            bejob=ap+besuffix

            #构建前端
            if server.job_exists(fejob):
                lastBuildNumber=server.get_job_info(fejob)['lastBuild']['number']
                buildResult=server.get_build_info(fejob,lastBuildNumber)['result']
                timetemp=server.get_build_info(fejob,lastBuildNumber)['timestamp']
                buildtimestamp=int(str(timetemp)[0:10])
                timeArray = time.localtime(buildtimestamp)
                buildTime=time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                print "构建项目: ",fejob
                print "构建时间: ",buildTime
                print "构建结果: ",buildResult


            if server.job_exists(h5job):
                lastBuildNumber=server.get_job_info(h5job)['lastBuild']['number']
                buildResult=server.get_build_info(h5job,lastBuildNumber)['result']
                timetemp=server.get_build_info(h5job,lastBuildNumber)['timestamp']
                buildtimestamp=int(str(timetemp)[0:10])
                timeArray = time.localtime(buildtimestamp)
                buildTime=time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                print "构建项目: ",h5job
                print "构建时间: ",buildTime
                print "构建结果: ",buildResult


            if server.job_exists(rpcjob):
                lastBuildNumber=server.get_job_info(rpcjob)['lastBuild']['number']
                buildResult=server.get_build_info(rpcjob,lastBuildNumber)['result']
                timetemp=server.get_build_info(rpcjob,lastBuildNumber)['timestamp']
                buildtimestamp=int(str(timetemp)[0:10])
                timeArray = time.localtime(buildtimestamp)
                buildTime=time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                print "构建项目: ",rpcjob
                print "构建时间: ",buildTime
                print "构建结果: ",buildResult


            if server.job_exists(bejob):
                lastBuildNumber=server.get_job_info(bejob)['lastBuild']['number']
                buildResult=server.get_build_info(bejob,lastBuildNumber)['result']
                timetemp=server.get_build_info(bejob,lastBuildNumber)['timestamp']
                buildtimestamp=int(str(timetemp)[0:10])
                timeArray = time.localtime(buildtimestamp)
                buildTime=time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                print "构建项目: ",bejob
                print "构建时间: ",buildTime
                print "构建结果: ",buildResult




if __name__=="__main__":
    configPath="config.ini"
    jkurl=""
    user=""
    passd=""
    fesuffix="-frontend"
    h5suffix="-h5"
    rpcsuffix="-service"
    besuffix="-backend"
    version="master"
    param_dict = {"commit_version": version}
    buildjob()
#    getBuildResult()