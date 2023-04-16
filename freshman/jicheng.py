class animal:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("吃")

class cat(animal):
    def catch(self):
        print("抓老鼠")

class dog(animal):
    # 类属性
    so='汪汪'
    def guard(self):
        print("看家")
    def __str__(self):
        return f"我是{self.name}，今年{self.age}岁"
class xdog(dog):
    def guard(self):
        super().guard()
        print("看家2222")


xiaohua = xdog("小花", 2)
print(xiaohua.so)
xiaohua.guard()
print(xiaohua)