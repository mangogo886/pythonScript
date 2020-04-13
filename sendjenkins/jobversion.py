#coding:utf-8

import urllib2
import json
import sys
import jenkins
import time

def get_job_version(job_name):
    server = jenkins.Jenkins('url', username='', password='')
    if server.job_exists(name=job_name):

        jobInfo = server.get_job_info(job_name)
        lastBuildNumber = server.get_job_info(job_name)['lastBuild']['number']
        Buildtemp = max(server.get_build_info(job_name, lastBuildNumber)['actions'])
        Buildversion=Buildtemp['lastBuiltRevision']['SHA1']
        tempTime=server.get_build_info(job_name,lastBuildNumber)['timestamp']
        buildtimestamp=int(str(tempTime)[0:10])
        timeArray = time.localtime(buildtimestamp)
        buildTime=time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        print "版本号:",Buildversion
        print "构建时间:",buildTime
    else:
        print job_name,"不存在，请检查job名称，重新输入执行..."


if __name__=='__main__':
    args1 = sys.argv[1]
    job_name="qky-"+args1
    get_job_version(job_name)