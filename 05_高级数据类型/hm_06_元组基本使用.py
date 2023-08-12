info_tuple = ("zhangsan", 18, 1.75, 18)

# 1.取值和取索引
# 取值
print(info_tuple[1])
# 取索引 已经知道数据的内容 想知道数据在元组中的索引
print(info_tuple.index(18))
# 2.统计计数
print(info_tuple.count(18))
# 统计元组中元素的个数
print(len(info_tuple))
