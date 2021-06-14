<!--
 * @Author: your name
 * @Date: 2021-06-14 22:08:55
 * @LastEditTime: 2021-06-14 22:15:00
 * @LastEditors: your name
 * @Description: 
 * @FilePath: \003_GitProject\Python\SystemOperation\将 list 写入一个 txt 文件四种方法.md
 * 可以输入预定的版权声明、个性签名、空行等
-->
# Python：将 list 写入一个 txt 文件四种方法

## 1  准备list文件
```python
a = [
    {"Jodie1": "123"},
    {"Jodie2": "456"},
    {"Jodie3": "789"},
    ]
```
## 2  要求输出txt文件的内容格式
写入到本地一个txt文件，内容格式如下：
```txt
Jodie1,123
Jodie2,456
Jodie3,789 """

import re
import json

a = [
    {"Jodie1": "123"},
    {"Jodie2": "456"},
    {"Jodie3": "789"},
    ]
```
## 3  方法如下
### 方法一
```python
with open('1.txt', 'w') as f:
    for i in range(len(a)):
        for key, values in a[i].items():
            print(key+","+values+"\r")
            f.write(key+","+values+"\r")
```
### 方法二
```python
file = open('2.txt', 'w')
for i in range(len(a)):
    s = str(a[i]).replace('{', '').replace('}', '').replace("'", '').replace(':', ',') + '\n'
    file.write(s)
file.close()
```
### 方法三
```python
file3 = open('3.txt', 'w')
for i in range(len(a)):
    s = (re.sub(r"['{ },]*", '', str(a[i])) + '\n').replace(':', ',')
    file3.write(s)
file3.close()
```
### 方法四
```python
with open('4.txt', 'w') as f:
    for i in range(len(a)):
        s = (re.sub(r"['{ },]*", '', str(a[i])) + '\n').replace(':', ',')
        f.write(s)
```