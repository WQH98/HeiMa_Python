class Animal:
    def eat(self):
        print("吃----")

    def drink(self):
        print("喝----")

    def run(self):
        print("跑----")

    def sleep(self):
        print("睡----")


class Dog(Animal):
    # 子类拥有父类的所有属性和方法
    def bark(self):
        print("叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("飞")


# 创建一个哮天犬的对象
xtq = XiaoTianQuan()
xtq.fly()
xtq.bark()
xtq.eat()
xtq.drink()
xtq.run()
xtq.sleep()