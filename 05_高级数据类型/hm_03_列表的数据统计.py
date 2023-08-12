name_list = ["宇智波斑", "宇智波泉奈", "宇智波佐助", "宇智波佐良娜", "宇智波斑"]

# len(length 长度) 函数可以统计列表中元素的总数
name_list_len = len(name_list)
print("列表中有 %d 个元素" % name_list_len)
# count方法可以统计列表中某一个数据出现的次数
count = name_list.count("宇智波斑")
print("斑爷出现了 %d 次" % count)
# 从列表删除数据 如果数据不存在 程序会报错
name_list.remove("宇智波斑")

print(name_list)
