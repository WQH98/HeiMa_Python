class Cat:

    def eat(self):
        # 哪一个对象调用的方法 self就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)


# 创建猫对象
tom = Cat()

# 可以使用 .属性名  利用赋值语句就可以了
tom.name = "Tom"

tom.eat()
tom.drink()

# 在日常开发中 不推荐在类的外部给对象增加属性 如果在运行时 没有找到属性 程序会报错
# 对象应该包含有哪些属性 应该封装在类的内部
