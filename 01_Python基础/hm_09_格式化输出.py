# 1.定义字符串变量name，输出 我的名字叫小明，请多多关照
name = "小明"
print("我的名字叫%s，请多多关照" % name)

# 2.定义整数变量student_no， 输出 我的学号是000001
student_no = 1
print("我的学号是%06d" % student_no)

# 3.定义小数price、weight、money，输出 苹果单价9.00元/斤，购买了5.00斤，需要支付45.00元
price = 9.00
weight = 5.00
money = price * weight
print("苹果单价%.2f元/斤，购买了%.2f斤，需要支付%.2f元" % (price, weight, money))

# 4.定义一个小数scale，输出 数据比例是10.00%
scale = 10.00
print("数据比例是%.2f%%" % scale)