name_list = ["斑", "泉奈", "佐助", "佐良娜", True, 111]

# 使用迭代遍历列表
"""
顺序的从列表中依次获取数据 每一次循环过程中 数据都会保存在my_name这个变量中
在循环体内部可以访问到当前这一次循环获取的数据

for my_name in 列表变量:
    print("我的名字叫%s" % my_name)

"""
for my_name in name_list:

    print("我的名字叫%s" % my_name)
