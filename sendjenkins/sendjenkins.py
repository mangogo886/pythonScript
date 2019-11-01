#!/usr/bin/env python
#coding:utf-8

import urllib2
import json
import sys

import jenkins
import time

reload(sys)
sys.setdefaultencoding('utf8')

def get_token(corp_id, secret):
    res = urllib2.urlopen('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (corp_id, secret))
    res_dict = json.loads(res.read())
    token = res_dict.get('access_token',False)
    #print token
    return token


def send_msg(content, to_user, to_party, to_tag, application_id, safe):
    token=get_token(corp_id, secret)
    try:
        data = {
            'touser': to_user,
            'toparty': to_party,
            'totag': to_tag,
            'msgtype':"text",
            "agentid":  application_id,
            "text":{"content": content},
            "safe": safe
        }
        data = json.dumps(data,ensure_ascii=False)
       # print data,type(data)
        req = urllib2.Request('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % (token,))
        resp = urllib2.urlopen(req,data)
        msg = u'返回值:'+resp.read()
    except Exception,ex:
        msg = u'异常:'+str(ex)
    finally:
        print msg

def get_buidl_info(job_name):

    server = jenkins.Jenkins('url',username='',password='')
    jobInfo = server.get_job_info(job_name)

    lastBuildNumber = server.get_job_info(job_name)['lastBuild']['number']
    BuildVersion=server.get_build_info(job_name,lastBuildNumber)['actions'][1]['lastBuiltRevision']['SHA1']
    lastBuildResult = server.get_build_info(job_name,lastBuildNumber)['result']
    tempTime=server.get_build_info(job_name,lastBuildNumber)['timestamp']
    buildtimestamp=int(str(tempTime)[0:10])
    timeArray = time.localtime(buildtimestamp)
    buildTime=time.strftime("%Y-%m-%d %H:%M:%S", timeArray)


    result_into="job_name: "+job_name+"\n"+"version: "+BuildVersion+"\n"+"result: "+lastBuildResult+"\n"+"buildtime: "+buildTime

    return result_into

if __name__=='__main__':
    corp_id='wx8a57906aa7f1ae98'
    secret='_iaWiNoeDHraPwm75V1v_bJEkN1ivFHgzFNoniKcSz8'
    job_name = sys.argv[1]
    to_user='zhumin'
    to_party='2'
    to_tag='@all'
    application_id='1'
    safe='0'
    content=get_buidl_info(job_name)
    get_token(corp_id, secret)
    send_msg(content, to_user, to_party, to_tag, application_id, safe)