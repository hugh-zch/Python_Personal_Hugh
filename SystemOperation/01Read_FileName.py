'''
Author: your name
Date: 2021-06-14 19:32:43
LastEditTime: 2021-06-14 23:06:48
LastEditors: your name
Description: 
FilePath: \003_GitProject\Python\Python_Personal_Hugh\SystemOperation\01Read_FileName.py
可以输入预定的版权声明、个性签名、空行等
'''
#coding=utf-8
'''
使用函数os.dirlist()读取文件夹内的文件名字
2015.08.06
'''
import os
#path = os.getcwd() # 获取程序所在文件夹路径
path ='E:/002 学习资料/007嵌入式开发学习资料/003 Stm32\视频教程/1-入门篇'
print('程序所在文件夹路径是：'+path)

files = os.listdir(path) # 获取指定路径下的所有文件的文件名称
print (files)
