# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import *
import urllib2
import json
import sys
import log
# Create your views here.



def apis(request):
    data1 = {}
    if request.method=="POST":
        #data=json.loads(request.body)
        data1=request.POST['tops']





        #print type(data1)
        #print data1
        log.logger.info(data1)
    return JsonResponse({'msg':data1})



corp_id='wx8a57906aa7f1ae98'
secret='_iaWiNoeDHraPwm75V1v_bJEkN1ivFHgzFNoniKcSz8'
def get_token(corp_id, secret):
    res = urllib2.urlopen('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (corp_id, secret))
    res_dict = json.loads(res.read())
    token = res_dict.get('access_token',False)
    #print token
    return token

def send_msg(request):
    token = get_token(corp_id, secret)
    to_party = '2'
    to_tag = '@all'
    application_id = '1'
    safe = '0'
    if request.method=='POST':
        #json_data=json.loads(request.body,encoding='utf-8')
        #context=json_data['content']
        #to_user=json_data['tops']
        context =request.POST['content']
        to_user = request.POST['tos']


        data = {
            'touser': to_user,
            'toparty': to_party,
            'totag': to_tag,
            'msgtype': "text",
            "agentid": application_id,
            "text": {"content": context},
            "safe": safe
        }
        #data = json.dumps(data, ensure_ascii=False)
        data = json.dumps(data)
        #print data, type(data)
        req = urllib2.Request('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % (token,))
        resp = urllib2.urlopen(req, data)
        msg = u'返回值:' + resp.read()
        return HttpResponse(data)

