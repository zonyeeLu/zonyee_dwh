#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************************************
# 程序名称:     practise_word_count.py
# 功能描述:     用python做单词统计
# 输入参数:     无
# 创建人名:     zonyee_lu
# 创建日期:     20190718
# ******************************************************************************
# ******************************************************************************

from bs4 import BeautifulSoup
import requests
import re

def main():
    dict = {}
    word_file = open("D:\\temp\\word.txt",'r+',encoding="utf-8")
    for line in word_file:
        word_list = line.replace('\n','').split(',')
        for word in word_list:
            if word in dict:
                dict[word] = dict[word]+1
            else:
                dict[word] = 1
    # 顺序排
    dict_test1 =  sorted(dict.items(),key=lambda x:x[1])
    print(dict_test1)

    # 倒序排
    dict_test2 = sorted(dict.items(), key=lambda x: x[1],reverse=True)
    print(dict_test2)


# main
if __name__ == '__main__':
    main()