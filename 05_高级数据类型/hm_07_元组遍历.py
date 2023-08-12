info_tuple = ("zhangsan", 18, 1.75, 18)

# 使用迭代遍历元组
for num in info_tuple:
    # 使用格式字符串拼接变量是不方便的
    # 因为元组中保存的数据类型通常是不相同的
    print(num)

info = ("zhangsan", 18, 1.75)
print("%s今年%d岁了,身高为%.2f米" % info)

