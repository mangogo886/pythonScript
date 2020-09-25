#!/usr/bin/env python
#coding:utf-8

import sys
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
    elif list=="qlyz":
        name="清流一中"
    elif list=="cq18":
        name="重庆18中"
    elif list=="gzqh":
        name="贵阳清华中学"
    else:
        name="没有匹配名字"

    return name
