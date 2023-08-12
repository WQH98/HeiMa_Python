# 格式化字符串后面的()本质上就是元组

info = ("zhangsan", 18)
print("%s的年龄是%d" % info)
info_str = "%s的年龄是%d" % info
print(info_str)
