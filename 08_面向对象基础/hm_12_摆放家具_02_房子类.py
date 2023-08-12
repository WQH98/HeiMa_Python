class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加 %s" % item)
        # 判断家具的面积
        if item.area > self.free_area:
            print("%s 的面积太大了 无法添加" % item.area)
            return
        self.free_area -= item.area
        self.item_list.append(item.name)


# 创建家具
bed = HouseItem("席梦思", 40)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 20)

# 创建房子对象
my_home = House("两室一厅", 60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)

# 主程序只负责创建房子对象和家具对象
# 让房子对象调用app_item方法将家具添加到房子中
# 面积计算 剩余面积 家具列表等处理都被封装到房子类的内部
