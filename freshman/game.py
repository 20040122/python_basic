import random
class Game:
    top_score = 0
    def __init__(self,name):
        self.name = name
    @staticmethod
    def show_help():
        print("帮助信息")
    @classmethod
    def show_top_score(cls):
        return cls.top_score
    def start_game(self):
        num=random.randint(10,101)
        print(f"{self.name}的分数是{num}")
        if num>Game.top_score:
            Game.top_score=num

a=Game("小明")
a.start_game()
a.start_game()
Game.show_help()
print(f"小明的最高分是{Game.top_score}")

