class Animal:
    def eat(self):
        print("吃----")

    def dring(self):
        print("喝----")

    def run(self):
        print("跑----")

    def sleep(self):
        print("睡----")


class Dog(Animal):
    # 子类拥有父类的所有属性和方法
    def bark(self):
        print("叫")


# 创建一个对象 - 狗对象
wangcai = Dog()
wangcai.eat()
wangcai.dring()
wangcai.run()
wangcai.sleep()
wangcai.bark()
