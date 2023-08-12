# 需求：小猫爱吃鱼 小猫要喝水
# 分析
# 1 定义一个猫类cat
# 2 定义两个方法eat和drink
# 3 按照需求--不要定义属性

class Cat:
    def eat(self):
        # 哪一个对象调用的方法 self就是哪一个对象的引用
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()
# 可以使用  .属性名  利用赋值语句就可以了
# 这种方式虽然简单 但是不推荐使用 因为这种方式没有对类的代码进行修改
tom.name = "Tom"

tom.eat()
tom.drink()
print(tom)

# 再创建一个猫对象
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

# 在类封装的方法内部 self就表示当前调用方法的对象自己
# 调用方法时 程序员不需要传递self参数
# 在方法内部 1 可以通过self访问对象的属性 2 也可以通过self调用其他的对象方法

