from datetime import datetime, timedelta

x = datetime.now()
y = x.strftime("%Y/%m/%d %H:%M:%S")  # 格式化時間，會轉成字串格式
print(type(x))
print(x)
print(type(y))
print(y)


# 把datetime object內部的值抓出來的方法
print(type(x.year))
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)


print("---------------")

a = datetime.now()
b = datetime(2021, 1, 19, 14)  # 年月日沒有dafult，為必填值
c = a-b
print(type(c))  # <class 'datetime.timedelta'>
print(c)
# 在timedalta內有read-only attribute,method
print(c.days)  # read-only attribute
print(c.total_seconds())  # read-only method


print("-------------")

now = datetime.now()
# timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
gap = timedelta(1)

tomorrow = now+gap
yesterday = now-gap
print(tomorrow)
print(yesterday)
print(tomorrow > yesterday)
