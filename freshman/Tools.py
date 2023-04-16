class Tool:
    count=0
    def __init__(self,name):
        self.name = name
        Tool.count += 1
    @classmethod
    def show_tools_count(cls):
        print("工具对象的数量 %d" % cls.count)

tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool1.show_tools_count()