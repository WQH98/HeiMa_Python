class Woman:
    def __init__(self, name):
        self.name = name
        # 私有属性
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部 是可以访问对象的私有属性的
        print("%s的年龄是%d" % (self.name, self.__age))


xiaofang = Woman("小芳")
# 私有属性 在外界不能直接访问
# print(xiaofang.__age)
# 私有方法 在外界不能直接访问
# xiaofang.__secret()
