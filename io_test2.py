import datetime
sName = input("请输入您的姓名：")
birthyear = int(input("请输入您的出生年份："))
age = datetime.date.today().year - birthyear  # 难点：获得当前年份
print("您好！{0}。您{1}岁。".format(sName, age))
