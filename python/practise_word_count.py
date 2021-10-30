#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************************************
# 程序名称:     practise_word_count.py
# 功能描述:     用python做单词统计
# 输入参数:     无
# 创建人名:     zonyee_lu
# 创建日期:     20190718
# ******************************************************************************
# 修改日期:     20211031
# 修改人:       zonyee_lu
# 修改内容:     新增模拟map、reduce阶段
#              shuffle过程解释 https://blog.csdn.net/ASN_forever/article/details/81233547
#              因为频繁的磁盘I/O操作会严重的降低效率，因此“中间结果”不会立马写入磁盘，而是优先存储到map节点的“环形内存缓冲区”，在写入的过程中进行分区（partition），也就是对于每个键值对来说，都增加了一个partition属性值，然后连同键值对一起序列化成字节数组写入到缓冲区（缓冲区采用的就是字节数组，默认大小为100M）。当写入的数据量达到预先设置的阙值后（mapreduce.map.io.sort.spill.percent,默认0.80，或者80%）便会启动溢写出线程将缓冲区中的那部分数据溢出写（spill）到磁盘的临时文件中，并在写入前根据key进行排序（sort）和合并（combine，可选操作）。溢出写过程按轮询方式将缓冲区中的内容写到mapreduce.cluster.local.dir属性指定的目录中。当整个map任务完成溢出写后，会对磁盘中这个map任务产生的所有临时文件（spill文件）进行归并（merge）操作生成最终的正式输出文件，此时的归并是将所有spill文件中的相同partition合并到一起，并对各个partition中的数据再进行一次排序（sort），生成key和对应的value-list，文件归并时，如果溢写文件数量超过参数min.num.spills.for.combine的值（默认为3）时，可以再次进行合并。至此，map端shuffle过程结束，接下来等待reduce task来拉取数据。对于reduce端的shuffle过程来说，reduce task在执行之前的工作就是不断地拉取当前job里每个map task的最终结果，然后对从不同地方拉取过来的数据不断地做merge最后合并成一个分区相同的大文件，然后对这个文件中的键值对按照key进行sort排序，排好序之后紧接着进行分组，分组完成后才将整个文件交给reduce task处理。

# ******************************************************************************

# from bs4 import BeautifulSoup
# import requests
# import re

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

# map函数读取文件,进行切割,并且输出键值对('word':1)
def map(input_file):
    # word_dict = {}
    # word_list 用于保存map输出,如('kobe',1)
    word_list=[]
    with open(input_file,'r+',encoding="utf-8") as file :
        for line in file:
            line = line.replace('\n','').split(',')
            for word in line:
                dict={}
                dict[word] = 1
                word_list.append(dict)
                # word_dict.setdefault(word,[]).append(1)
    # print(word_list)
    return word_list

def shuffle(word_list):
    # 归并map端的输出,结果['word':[1,1,1]]
    word_dict = {}
    for word in word_list:
        for w in word: 
            word_dict.setdefault(w,[]).append(word[w])
    print(word_dict)
    return word_dict 

def reduce(word_dict):
    # 计算单次数
    result={}
    for word in word_dict:
        sum = 0
        for count in word_dict[word]:
            sum = sum+count 
        result[word]=sum
    print(result)
# main
if __name__ == '__main__':
    word_dict = shuffle(map("D:\\temp\\word.txt"))
    reduce(word_dict)