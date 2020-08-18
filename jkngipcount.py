#!/usr/bin/env python
#coding:utf-8

import urllib2
import json
import sys
import requests
import time
import paramiko
import os
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
        msg = resp.read()
    except Exception,ex:
        msg = str(ex)
    finally:
        print msg

def ipcount():
              
    hostname='ysx1'
    username='...'
    ssh=paramiko.SSHClient()
    ssh.load_system_host_keys()
    privatekey=os.path.expanduser('/.../.../.ssh/id_rsa')
    key=paramiko.RSAKey.from_private_key_file(privatekey)
    ssh.connect(hostname=hostname,username=username,pkey=key)
    cmd='/data/ops/script/jkngip.sh'
    stdin,stdout,stderr=ssh.exec_command(cmd)
    Results=stdout.readlines()
    content=""
    if len(Results):
        for i in Results:
            ips=i.strip().encode().split()
            if int(ips[0])>=100:
                url1="http://ip-api.com/json/"
                url2="?lang=zh-CN"
                url=url1+ips[1]+url2
                response=requests.get(url)
                data=response.text
                city=json.loads(data)['city'].encode('utf-8')
                country=json.loads(data)['country'].encode('utf-8')
                isp=json.loads(data)['isp'].encode('utf-8')
                content=content+ips[0]+": "+ips[1]+country+city+isp+"\n"
        get_token(corp_id, secret)
        send_msg(content, to_user, to_party, to_tag, application_id, safe)
    else:
        print "not ip list..."
    ssh.close()

if __name__=='__main__':
    corp_id='wx8a57906aa7f1ae98'
    secret='_iaWiNoeDHraPwm75V1v_bJEkN1ivFHgzFNoniKcSz8'
    to_user='zhumin'
    to_party='2'
    to_tag='@all'
    application_id='1'
    safe='0'
    api_url = "http://ip.taobao.com/service/getIpInfo.php"
    ipcount()