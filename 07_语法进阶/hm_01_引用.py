def test(num):
    # 结论：python不允许程序员选择采用传值还是传引用。Python参数传递采用的肯定是“传对象引用”的方式。
    # 这种方式相当于传值和传引用的一种综合。
    # 如果函数收到的是一个可变对象（比如字典或者列表）的引用，就能修改对象的原始值
    # 相当于通过“传引用”来传递对象。
    # 如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用，
    # 结论：python不允许程序员选择采用传值还是传引用。Python参数传递采用的肯定是“传对象引用”的方式。
    # 这种方式相当于传值和传引用的一种综合。如果函数收到的是一个可变对象（比如字典或者列表）的引用
    # 就能修改对象的原始值－－相当于通过“传引用”来传递对象。如果函数收到的是一个不可变对象
    # （比如数字、字符或者元组）的引用，就不能直接修改原始对象－－相当于通过“传值'来传递对象。
    print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))
    # 定义一个字符串变量
    result = "hello"
    print("函数要返回的内存地址是 %d" % id(result))
    # 将字符串变量返回 返回的是数据的引用 而不是数据本身
    return result


# 1.定义一个数字的变量
a = 10

# 数据的地址本质上就是一个数字
print("a 变量保存数据的内存地址是 %d" % id(a))

# 2.调用 test 函数 本质上传递的是实参保存数据的引用 而不是实参保存的数据
# 注意：如果函数有返回值 但是没有定义变量接收
# 程序不会报错 但是无法获得返回结果
r = test(a)
print("%s 的内存地址是 %d" % (r, id(r)))
