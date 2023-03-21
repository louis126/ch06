'''
Author: LTX && 246823131@qq.com
Date: 2023-01-18 11:04:05
LastEditors: LTX && 246823131@qq.com
LastEditTime: 2023-01-18 11:09:55
FilePath: \ch06\type_file5.py
Description:'read(size)当size不指定时, 会将文件全部内容读取, size是字符数

readline()一次只读取一行即遇到'\n'返回

readlines()读取整个文件，并返回列表，一行为一个元素'

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved.
'''
f = open('C:\\pythonna\\ch01\\open.txt', 'r', encoding='utf-8')
a = f.read(100)
print(a)
f.close()
