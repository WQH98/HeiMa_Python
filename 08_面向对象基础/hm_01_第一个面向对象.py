# 需求：小猫爱吃鱼 小猫要喝水
# 分析
# 1 定义一个猫类cat
# 2 定义两个方法eat和drink
# 3 按照需求--不要定义属性

class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()

tom.eat()
tom.drink()
