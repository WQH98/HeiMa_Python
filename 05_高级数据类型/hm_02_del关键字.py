name_list = ["宇智波斑", "宇智波泉奈", "宇智波佐助"]

# （知道）使用del关键字delete删除列表元素
# 提示：日常开发中，要从列表删除数据，建议使用列表提供的方法
del name_list[1]

# del关键字本质上是将一个变量从内存中删除
name = "小明"
# 注意：如果使用del关键字删除变量
# 后续程序就不能再使用这个变量了
del name

print(name_list)
