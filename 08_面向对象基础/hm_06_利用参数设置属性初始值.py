# 在开发中 如果希望在创建对象的同时 就设置对象的属性 可以对__init__方法进行改造
#   1把希望设置的属性值 定义成__init__方法的参数
#   2在方法内部使用self.属性 = 形参接受外部传递的参数
#   3在创建对象时 使用类名(属性1,属性2...)调用


class Cat:
    def __init__(self, new_name):
        print("这是一个初始化方法")

        # self.属性名 = 属性的初始值
        self.name = new_name

    def eat(self):
        print("%s 爱吃鱼" % self.name)


# 使用类名()创建对象的时候 会自动调用初始化方法__init__
tom = Cat("Tom")

print(tom.name)

lazy_cat = Cat("大懒猫")
lazy_cat.eat()
