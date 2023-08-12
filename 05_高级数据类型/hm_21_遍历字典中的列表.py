students = [
            {
                "name": "阿土",
                "age": 20,
                "gender": True,
                "height": 1.75,
                "weight": 75
            },
            {
                "name": "小美",
                "age": 19,
                "gender": False,
                "height": 1.6,
                "weight": 45
            }
]

find_name = "阿土"

for stu_dict in students:

    print(stu_dict)

    if stu_dict["name"] == find_name:
        print("OK 找到了 %s" % find_name)
        # 如果已经找到 应该直接退出循环 不再遍历后面的元素
        break
# 如果希望在搜索列表时 所有的列表检查完成后 没有发现搜索目标 还希望得到一个统一的提示
else:
    print("not find %s" % find_name)

print("finish")
