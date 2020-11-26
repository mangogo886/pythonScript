#!/usr/bin/env python
#coding:utf-8

import os

filenames=open('files').readlines()
for file in filenames:
    file=file.strip()
    os.popen("sed -i '/        error_page 405 =200 $uri;/a\        ' %s" %file)
