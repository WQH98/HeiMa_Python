name_list = ["zhangsan", "lisi", "wangwu"]

# 1.取值和取索引
# 取值
print(name_list[2])
# 取索引
print(name_list.index("zhangsan"))
# 2.修改
name_list[1] = "李四"

# 3.增加
# append方法可以向列表的末尾增加数据
name_list.append("王小二")
# insert方法可以向列表指定索引位置增加数据
name_list.insert(1, "宇智波斑")
# extend方法可以把一个完整的列表追加到当前列表末尾
temp_list = ["千手柱间", "千手扉间", "猴子"]
name_list.extend(temp_list)
# 4.删除
# remove方法可以从列表中删除指定数据
name_list.remove("李四")
# pop方法默认把列表最后一个元素删除
name_list.pop()
# pop方法可以制定删除的索引
name_list.pop(2)
# clear方法可以清空列表
name_list.clear()

print(name_list)
