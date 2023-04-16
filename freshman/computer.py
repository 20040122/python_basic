class computer:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def playm(self,name):
        self.name=name
    def __str__(self):
        return f"价格为{self.price}的{self.brand}电脑播放{self.name}"

a=computer("小米",4000)
b=computer("苹果",10000)

a.playm("葫芦娃")
b.playm("变形金刚")

print(a)
print(b)