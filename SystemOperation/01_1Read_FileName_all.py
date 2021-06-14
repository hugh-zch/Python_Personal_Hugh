'''
Author: Hugh_zch
Date: 2021-06-14 20:56:32
LastEditTime: 2021-06-14 22:46:34
LastEditors: your name
Description: 读取文件夹下所有文件内的文件名，并且输出markdown格式
FilePath: \003_GitProject\Python\SystemOperation\01_1Read_FileName_all.py
可以输入预定的版权声明、个性签名、空行等
'''
#coding=utf-8
# -*- coding: utf-8 -*-
import os
import re
import numpy as np

path ='E:/002 学习资料/007嵌入式开发学习资料/003 Stm32/视频教程/1-视频'# 指定路径
files = os.listdir(path) # 获取指定路径下的所有文件的文件名称
# print(path +'/')
x =0
filename2 =[]
for file in files:#for循环遍历files的每个元素
    path0 = path +'/'+ file# 把元素加到path后面，形成新的路径
    files = os.listdir(path0)# 读取新路径上的每个文件的名字，形成列表
    n = len(files)# 计算列表的长度
    for i in range(0,n):#通过for循环遍历列表上的每个元素
        filename1 = files[i]
        head, sep, tail = filename1.partition('.')#通过函数partition，字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串
        files[i] = head#把第一个元祖的元素重新导入到files的列表上，实现删除“点”后面的格式
        # files[i] = '##  '+head #输出markdown格式的列表
    filename2 =filename2 +files
    list = np.unique(filename2)#使用np.unique函数进行去重

# 输出文件
with open('stm32的文件.txt', 'w') as f:
    for i in range(len(list)):
        s = str(list[i])+ '\n'
        f.write(s)