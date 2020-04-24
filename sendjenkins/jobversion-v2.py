#!/usr/bin/env python
#coding:utf-8

import urllib2
import json
import sys
import jenkins
import time
import ConfigParser

def get_jkurl(priurl):
    confurl="urls.ini"
    cf = ConfigParser.ConfigParser()
    cf.read(confurl)
    try:
        opts = cf.get(priurl, 'url')
        pri_jk_url=opts.strip()
        return pri_jk_url
    except Exception, e:
        print "环境参数不正确，请检查后再重新查询...",priurl
        return 0

def get_job_version(na):
    jkurl=get_jkurl(priurl)
    if jkurl==0:
        return
    else:
        try:
            server = jenkins.Jenkins(jkurl, username='', password='')
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
                                    print "部署环境:",priurl
                                    print "项目名称:",job_name
                                    print "版本号:",Buildversion
                                    print "构建时间:",buildTime
        except Exception, e:
            print "jenkins地址无法登录:",jkurl

if __name__=='__main__':
    priurl = sys.argv[1]
    na = sys.argv[2]
    get_job_version(na)