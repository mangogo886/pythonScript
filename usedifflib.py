#!/usr/bin/env python
#coding:utf8
#对比文件内容差异，生成html

import difflib
import sys

# 读取建表语句或配置文件
def read_file(file_name):
    try:
        file_desc = open(file_name, 'r')
        # 读取后按行分割
        text = file_desc.read().splitlines()
        file_desc.close()
        return text
    except IOError as error:
        print 'Read input file Error: {0}'.format(error)
        sys.exit()

# 比较两个文件并把结果生成一份html文本
def compare_file(file1, file2):
    if len(sys.argv) < 2:
        print "entry compare filename..."
    else:
        text1_lines = read_file(file1)
        text2_lines = read_file(file2)
        diff = difflib.HtmlDiff()    # 创建HtmlDiff 对象
        result = diff.make_file(text1_lines, text2_lines)  # 通过make_file 方法输出 html 格式的对比结果
    # 将结果写入到result_comparation.html文件中
    try:
        with open('result_comparation.html', 'w') as result_file:
            result_file.write(result)
            print "0==}==========> Successfully Finished\n"
    except IOError as error:
        print '写入html文件错误：{0}'.format(error)

if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    compare_file(file1, file2)