import hm_01_测试模块1 as DogModule
import hm_02_测试模块2 as CatModule

DogModule.say_hello()
CatModule.say_hello()

# 使用打印输出时 会打印出原有名称来
# 使用as只是更换本文件中的名字
dog = DogModule.Dog()
print(dog)
cat = CatModule.Cat()
print(cat)
