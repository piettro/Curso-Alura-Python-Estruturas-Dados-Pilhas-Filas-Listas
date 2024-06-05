from stack import Stack


class Level:

    def __init__(self, cenario, points, punishiment):
        self.cenario = cenario
        self.points = points
        self.punishiment = punishiment

    def __repr__(self):
        return self.cenario


def main():
    levels = Stack()
    level_1 = Level("Floresta", 300, -100)
    level_2 = Level("Castelo", 100, -4)
    level_3 = Level("Caverna", 400, -50)
    level_4 = Level("Guerra", 3000, -400)

    levels.stacking(level_1)
    levels.stacking(level_2)
    levels.stacking(level_3)
    levels.stacking(level_4)

    fail = levels.unstacking()
    print("Fail in level:")
    print(fail)
    fail = levels.unstacking()
    print("Fail in level:")
    print(fail)
    print("Back to level")
    print(levels.topo)



main()