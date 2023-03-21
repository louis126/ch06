'''
Author: LTX && 246823131@qq.com
Date: 2023-01-18 10:24:12
LastEditors: LTX && 246823131@qq.com
LastEditTime: 2023-01-18 10:26:37
FilePath: \ch06\type_file1.py
Description: 'c语言编程网讲解open函数'

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved.
'''
# 以默认方式打开文件
f = open('C:\\pythonna\\ch01\\open.txt')
# 输出文件是否已经关闭
print(f.closed)
# 输出访问模式
print(f.mode)
# 输出编码格式
print(f.encoding)
# 输出文件名
print(f.name)
