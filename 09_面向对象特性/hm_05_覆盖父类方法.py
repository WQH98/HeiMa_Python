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
        print("狗叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("飞")

    def bark(self):
        print("叫的跟神一样...")


xtq = XiaoTianQuan()
# 如果在子类中 重写了父类的方法
# 在使用子类对象调用方法时 会调用子类中重写的方法
xtq.bark()

