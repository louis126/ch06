'''
Author: LTX && 246823131@qq.com
Date: 2023-01-18 10:56:00
LastEditors: LTX && 246823131@qq.com
LastEditTime: 2023-01-18 11:01:44
FilePath: \ch06\type_file4.py
Description: 'CSDN'

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved.
'''
f = open('C:\\pythonna\\ch01\\open.txt', 'r', errors='ignore')  # 打开一个文件，将这个操作赋予给一f = open('../all.txt','r',errors = 'ignore')
a = f.read()
print(type(f))
print(type(a))
print(a)
f.close()
