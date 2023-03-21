'''
Author: LTX && 246823131@qq.com
Date: 2023-01-17 17:19:08
LastEditors: LTX && 246823131@qq.com
LastEditTime: 2023-01-17 19:39:08
FilePath: \ch06\stat.py
Description:
Copyright (c) 2023 by ${git_name_email}, All Rights Reserved.
'''
a = []
x = float(input("请输入一个实数，输入-1中止："))
while x != -1:
    a.append(x)
    x = float(input("请输入一个实数，输入-1中止："))
print("计数：", len(a))
print("求和：", sum(a))
print("均值：", sum(a)/len(a))
