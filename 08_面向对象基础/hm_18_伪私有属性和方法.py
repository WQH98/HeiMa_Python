class Woman:
    def __init__(self, name):
        self.name = name
        # 私有属性
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部 是可以访问对象的私有属性的
        print("%s的年龄是%d" % (self.name, self.__age))


xiaofang = Woman("小芳")

print(xiaofang._Woman__age)

xiaofang._Woman__secret()
