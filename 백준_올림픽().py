from functools import cmp_to_key


class Obj:
    def __init__(self, n, g, s, b):
        self.number = n
        self.gold = g
        self.silver = s
        self.bronze = b

    def obj_print(self):
        print(self.number, self.gold, self.silver, self.bronze)


def mycmp(a, b):
    if a.gold > b.gold:
        return -1
    elif a.gold < b.gold:
        return 1
    else:
        if a.silver > b.silver:
            return -1
        elif a.silver < b.silver:
            return 1
        else:
            if a.bronze > b.bronze:
                return -1
            elif a.bronze < b.bronze:
                return 1
            else:
                return 0


A = Obj(1, 2, 2, 3)
B = Obj(2, 1, 3, 6)
C = Obj(3, 1, 3, 6)
D = Obj(4, 0, 2, 3)

my_list = [D, C, A, B]
my_list.sort(key=cmp_to_key(mycmp))
for m in my_list:
    m.obj_print()
