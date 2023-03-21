'''
Author: LTX && 246823131@qq.com
Date: 2023-01-18 10:08:23
LastEditors: LTX && 246823131@qq.com
LastEditTime: 2023-01-18 10:22:30
FilePath: \ch06\type_file.py
Description:'文件的打开、读取与输出'

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved.
'''
import sys
filename = sys.argv[0]
f = open(filename, 'r', encoding='utf8')
line_no = 0
while True:
    line_no += 1
    line = f.readline()
    if line:
        print(line_no, ":", line)
    else:
        break
f.close()
