#!/usr/bin/env python
#coding:utf-8


import urllib2
import json
import sys
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
        print data,type(data)
        req = urllib2.Request('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % (token,))
        resp = urllib2.urlopen(req,data)
        msg = u'返回值:'+resp.read()
    except Exception,ex:
        msg = u'异常:'+str(ex)
    finally:
        print msg

if __name__=='__main__':
    corp_id='wx8a57906aa7f1ae98'
    secret='_iaWiNoeDHraPwm75V1v_bJEkN1ivFHgzFNoniKcSz8'
    content="测试告警"
    to_user='zhumin'
    to_party='2'
    to_tag='@all'
    application_id='1'
    safe='0'
    get_token(corp_id, secret)
    send_msg(content, to_user, to_party, to_tag, application_id, safe)


