'''
Author: LTX && 246823131@qq.com
Date: 2023-01-18 10:36:47
LastEditors: LTX && 246823131@qq.com
LastEditTime: 2023-01-18 10:52:08
FilePath: \ch06\type_file3.py
Description: '脚本之家教程'

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved.
'''
name = open('C:\\pythonna\\ch01\\open.txt', 'w+')
name.write("s")  # 写入一个字符s
name.close()  # 此时尚未真正写入，还只是存在于内存中。
name = open("C:\\pythonna\\ch01\\open.txt")
print(name.read())
name.close()
