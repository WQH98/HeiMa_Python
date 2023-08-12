class Gun:
    def __init__(self, model, bullet_count):
        self.model = model
        self.bullet_count = bullet_count

    def add_bullet(self, count):
        self.bullet_count += count
        print("加弹成功 目前有%d发子弹" % self.bullet_count)

    def shoot(self):
        if self.bullet_count <= 0:
            print("没有子弹了")
            return
        self.bullet_count -= 1
        print("目前有%d发子弹" % self.bullet_count)


class Solder:
    def __init__(self, name, model, bullet_count):
        self.name = name
        self.gun = Gun(model, bullet_count)

    def fire(self):
        print("%s的%s响了" % (self.name, self.gun.model))
        self.gun.shoot()


xusanduo = Solder("许三多", "AK47", 100)
xusanduo.fire()
xusanduo.gun.add_bullet(10)

