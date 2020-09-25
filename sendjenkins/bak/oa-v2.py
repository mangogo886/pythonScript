#!/usr/bin/env python
##coding:utf-8

import jenkins
import os
import sys
import time
import threading
reload(sys)
sys.setdefaultencoding( "utf-8" )

def jsy():
    jenkins_url=""
    try:
        server=jenkins.Jenkins(jenkins_url,username=user_id,password=api_token)
        server.build_job(job_name,parameters=param_dict)
        lastBuildNumber = server.get_job_info(job_name)['lastBuild']['number']
        buil = server.get_build_info(job_name, lastBuildNumber)['building']
        #判断是否正在构建
        print "金山云OA正在构建....."
        while buil:
            time.sleep(1)
            buil = server.get_build_info(job_name, lastBuildNumber)['building']

        console=server.get_build_console_output(job_name,lastBuildNumber)
        tempTime = server.get_build_info(job_name, lastBuildNumber)['timestamp']
        buildtimestamp = int(str(tempTime)[0:10])
        timeArray = time.localtime(buildtimestamp)
        buildTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        BuildVersion = server.get_build_info(job_name, lastBuildNumber)['actions'][2]['lastBuiltRevision']['SHA1']
        print "版本号：",BuildVersion
        print "金山云构建时间：",buildTime
        print "金山云最新构建序号：",lastBuildNumber
        print "金山云OA--构建日志：",console
    except Exception, e:
        print "金山云登录失败:", e

def qlyz():
    jenkins_url=""
    try:
        server=jenkins.Jenkins(jenkins_url,username=user_id,password=api_token)
        server.build_job(job_name,parameters=param_dict)
        lastBuildNumber = server.get_job_info(job_name)['lastBuild']['number']
        buil = server.get_build_info(job_name, lastBuildNumber)['building']
        # 判断是否正在构建
        print "清流一中OA正在构建....."
        while buil:
            time.sleep(1)
            buil = server.get_build_info(job_name, lastBuildNumber)['building']
        console=server.get_build_console_output(job_name,lastBuildNumber)
        tempTime = server.get_build_info(job_name, lastBuildNumber)['timestamp']
        buildtimestamp = int(str(tempTime)[0:10])
        timeArray = time.localtime(buildtimestamp)
        buildTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        BuildVersion = server.get_build_info(job_name, lastBuildNumber)['actions'][2]['lastBuiltRevision']['SHA1']
        print "版本号：", BuildVersion
        print "清流一中构建时间：",buildTime
        print "清流一中最新构建序号：",lastBuildNumber
        print "清流一中OA--构建日志：",console
    except Exception, e:
        print "清流一中登录失败:", e

def gm():
    jenkins_url=""
    try:
        server=jenkins.Jenkins(jenkins_url,username=user_id,password=api_token)
        server.build_job(job_name,parameters=param_dict)
        lastBuildNumber = server.get_job_info(job_name)['lastBuild']['number']
        buil = server.get_build_info(job_name, lastBuildNumber)['building']
        # 判断是否正在构建
        print "高密OA正在构建....."
        while buil:
            time.sleep(1)
            buil = server.get_build_info(job_name, lastBuildNumber)['building']
        console=server.get_build_console_output(job_name,lastBuildNumber)
        tempTime = server.get_build_info(job_name, lastBuildNumber)['timestamp']
        buildtimestamp = int(str(tempTime)[0:10])
        timeArray = time.localtime(buildtimestamp)
        buildTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        BuildVersion = server.get_build_info(job_name, lastBuildNumber)['actions'][2]['lastBuiltRevision']['SHA1']
        print "版本号：", BuildVersion
        print "高密构建时间：",buildTime
        print "高密最新构建序号：",lastBuildNumber
        print "高密OA--构建日志：",console
    except Exception, e:
        print "高密登录失败:", e

def xxyery():
    jenkins_url=""
    try:
        server=jenkins.Jenkins(jenkins_url,username=user_id,password=api_token)
        server.build_job(job_name,parameters=param_dict)
        lastBuildNumber = server.get_job_info(job_name)['lastBuild']['number']
        buil = server.get_build_info(job_name, lastBuildNumber)['building']
        # 判断是否正在构建
        print "湘西幼儿园OA正在构建....."
        while buil:
            time.sleep(1)
            buil = server.get_build_info(job_name, lastBuildNumber)['building']
        console=server.get_build_console_output(job_name,lastBuildNumber)
        tempTime = server.get_build_info(job_name, lastBuildNumber)['timestamp']
        buildtimestamp = int(str(tempTime)[0:10])
        timeArray = time.localtime(buildtimestamp)
        buildTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        BuildVersion = server.get_build_info(job_name, lastBuildNumber)['actions'][2]['lastBuiltRevision']['SHA1']
        print "版本号：", BuildVersion
        print "湘西幼儿园构建时间：",buildTime
        print "湘西幼儿园最新构建序号：",lastBuildNumber
        print "湘西幼儿园OA--构建日志：",console
    except Exception, e:
        print "湘西幼儿园登录失败:", e

def jdsyfx():
    jenkins_url=""
    try:
        server=jenkins.Jenkins(jenkins_url,username=user_id,password=api_token)
        server.build_job(job_name,parameters=param_dict)
        lastBuildNumber = server.get_job_info(job_name)['lastBuild']['number']
        buil = server.get_build_info(job_name, lastBuildNumber)['building']
        # 判断是否正在构建
        print "湘西小学OA正在构建....."
        while buil:
            time.sleep(1)
            buil = server.get_build_info(job_name, lastBuildNumber)['building']
        console=server.get_build_console_output(job_name,lastBuildNumber)
        tempTime = server.get_build_info(job_name, lastBuildNumber)['timestamp']
        buildtimestamp = int(str(tempTime)[0:10])
        timeArray = time.localtime(buildtimestamp)
        buildTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        BuildVersion = server.get_build_info(job_name, lastBuildNumber)['actions'][2]['lastBuiltRevision']['SHA1']
        print "版本号：", BuildVersion
        print "湘西小学构建时间：",buildTime
        print "湘西小学最新构建序号：",lastBuildNumber
        print "湘西小学OA--构建日志：",console
    except Exception, e:
        print "湘西小学登录失败:", e

def xxrjzx():
    jenkins_url=""
    try:
        server=jenkins.Jenkins(jenkins_url,username=user_id,password=api_token)
        server.build_job(job_name,parameters=param_dict)
        lastBuildNumber = server.get_job_info(job_name)['lastBuild']['number']
        buil = server.get_build_info(job_name, lastBuildNumber)['building']
        # 判断是否正在构建
        print "湘西中学OA正在构建....."
        while buil:
            time.sleep(1)
            buil = server.get_build_info(job_name, lastBuildNumber)['building']
        console=server.get_build_console_output(job_name,lastBuildNumber)
        tempTime = server.get_build_info(job_name, lastBuildNumber)['timestamp']
        buildtimestamp = int(str(tempTime)[0:10])
        timeArray = time.localtime(buildtimestamp)
        buildTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        BuildVersion = server.get_build_info(job_name, lastBuildNumber)['actions'][2]['lastBuiltRevision']['SHA1']
        print "版本号：", BuildVersion
        print "湘西中学构建时间：",buildTime
        print "湘西中学最新构建序号：",lastBuildNumber
        print "湘西中学OA--构建日志：",console
    except Exception, e:
        print "湘西中学登录失败:", e

def gzzhjyy():
    jenkins_url=""
    try:
        server=jenkins.Jenkins(jenkins_url,username=user_id,password=api_token)
        server.build_job(job_name,parameters=param_dict)
        lastBuildNumber = server.get_job_info(job_name)['lastBuild']['number']
        buil = server.get_build_info(job_name, lastBuildNumber)['building']
        # 判断是否正在构建
        print "黔东南OA正在构建....."
        while buil:
            time.sleep(1)
            buil = server.get_build_info(job_name, lastBuildNumber)['building']
        console=server.get_build_console_output(job_name,lastBuildNumber)
        tempTime = server.get_build_info(job_name, lastBuildNumber)['timestamp']
        buildtimestamp = int(str(tempTime)[0:10])
        timeArray = time.localtime(buildtimestamp)
        buildTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        BuildVersion = server.get_build_info(job_name, lastBuildNumber)['actions'][2]['lastBuiltRevision']['SHA1']
        print "版本号：", BuildVersion
        print "贵州黔东南构建时间：",buildTime
        print "贵州黔东南最新构建序号：",lastBuildNumber
        print "贵州黔东南OA--构建日志：",console
    except Exception, e:
        print "贵州黔东南登录失败:", e
def rqschool():

    jenkins_url=""
    try:
        server=jenkins.Jenkins(jenkins_url,username=user_id,password=api_token)
        server.build_job(job_name,parameters=param_dict)
        lastBuildNumber = server.get_job_info(job_name)['lastBuild']['number']
        buil = server.get_build_info(job_name, lastBuildNumber)['building']
        # 判断是否正在构建
        print "瑞泉OA正在构建....."
        while buil:
            time.sleep(1)
            buil = server.get_build_info(job_name, lastBuildNumber)['building']
        console=server.get_build_console_output(job_name,lastBuildNumber)
        tempTime = server.get_build_info(job_name, lastBuildNumber)['timestamp']
        buildtimestamp = int(str(tempTime)[0:10])
        timeArray = time.localtime(buildtimestamp)
        buildTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        BuildVersion = server.get_build_info(job_name, lastBuildNumber)['actions'][2]['lastBuiltRevision']['SHA1']
        print "版本号：", BuildVersion
        print "瑞泉构建时间：",buildTime
        print "瑞泉最新构建序号：",lastBuildNumber
        print "瑞泉OA--构建日志：",console
    except Exception, e:
        print "瑞泉登录失败:", e

def nsfzsq():
    jenkins_url=""
    try:
        server=jenkins.Jenkins(jenkins_url,username=user_id,password=api_token)
        server.build_job(job_name,parameters=param_dict)
        lastBuildNumber = server.get_job_info(job_name)['lastBuild']['number']
        buil = server.get_build_info(job_name, lastBuildNumber)['building']
        # 判断是否正在构建
        print "南师附中OA正在构建....."
        while buil:
            time.sleep(1)
            buil = server.get_build_info(job_name, lastBuildNumber)['building']
        console=server.get_build_console_output(job_name,lastBuildNumber)
        tempTime = server.get_build_info(job_name, lastBuildNumber)['timestamp']
        buildtimestamp = int(str(tempTime)[0:10])
        timeArray = time.localtime(buildtimestamp)
        buildTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        BuildVersion = server.get_build_info(job_name, lastBuildNumber)['actions'][2]['lastBuiltRevision']['SHA1']
        print "版本号：", BuildVersion
        print "南师附中构建时间：",buildTime
        print "南师附中最新构建序号：",lastBuildNumber
        print "南师附中OA--构建日志：",console
    except Exception,e:
        print "南师附中登录失败:",e

if __name__=='__main__':
    user_id = ""
    api_token = ""
    job_name = ''
    #version=raw_input("构建版本号:")
    version=sys.argv[1]
    param_dict = {"commit_version": version}
    threads=[threading.Thread(target=jsy),threading.Thread(target=qlyz),threading.Thread(target=gm),threading.Thread(target=xxyery),threading.Thread(target=jdsyfx),threading.Thread(target=xxrjzx),threading.Thread(target=gzzhjyy),threading.Thread(target=rqschool),threading.Thread(target=nsfzsq)]
    for t in threads:
        t.start()