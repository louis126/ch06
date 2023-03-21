'''
Author: LTX && 246823131@qq.com
Date: 2023-01-17 19:42:46
LastEditors: LTX && 246823131@qq.com
LastEditTime: 2023-01-18 09:43:49
FilePath: \ch06\getpass1.py
Description:

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved.
'''
import getpass
username = input("用户名：")
passwd = getpass.getpass("密码：")
if username == 'jiang' and passwd == 'password':
    print('登陆成功！')
else:
    print('登录失败')
