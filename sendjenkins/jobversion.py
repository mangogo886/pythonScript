#!/usr/bin/env python
#coding:utf-8

import urllib2
import json
import sys
import jenkins
import time

def get_job_version(na):
    server = jenkins.Jenkins('jkurl', username='', password='')
    jobs_list=server.get_all_jobs()
    for jobs in jobs_list:
        job_name_list=jobs['fullname']
        if job_name_list.startswith("qky-"):
            job_name=job_name_list
            if na in job_name:
                if server.job_exists(name=job_name):
                    jobInfo = server.get_job_info(job_name)
                    if server.get_job_info(job_name)['lastBuild'] is not None:
                        lastBuildNumber = server.get_job_info(job_name)['lastBuild']['number']
                        Buildtemp = max(server.get_build_info(job_name, lastBuildNumber)['actions'])
                        if Buildtemp.has_key('lastBuiltRevision'):
                            Buildversion=Buildtemp['lastBuiltRevision']['SHA1']
                            tempTime=server.get_build_info(job_name,lastBuildNumber)['timestamp']
                            buildtimestamp=int(str(tempTime)[0:10])
                            timeArray = time.localtime(buildtimestamp)
                            buildTime=time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                            print "项目名称:",job_name
                            print "版本号:",Buildversion
                            print "构建时间:",buildTime
                else:
                    print job_name,"不存在，请检查job名称，重新输入执行..."


if __name__=='__main__':
    na = sys.argv[1]
    get_job_version(na)