class houseitem:
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        return f"{self.name}占地{self.area}平米"

bed=houseitem("席梦思",4)
chest=houseitem("衣柜",2)
table=houseitem("餐桌",1.5)

class house:
    def __init__(self,h_type,area):
        self.h_type=h_type
        self.total_area=area
        self.free_area=area
        self.item_list=[]

    def add_item(self,item):
        if self.free_area>item.area:
            print(f"添加{item.name}")
            self.item_list.append(item.name)
        else:
            print("添加失败")
        self.free_area-=item.area

    def __str__(self):
        return f"户型：{self.h_type}，总面积：{self.total_area}平米，剩余面积：{self.free_area}平米，家具：{self.item_list}"



myhouse=house("两室一厅",60)
myhouse.add_item(table)
myhouse.add_item(bed)
print(myhouse)
