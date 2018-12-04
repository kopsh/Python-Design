import random
from enum import Enum

TreeType = Enum('TreeType', "apple cherry peach")


class Tree:
    pool = dict()

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age):
        print('render a tree of type {} and age {}'.format(self.tree_type, age))


def main():
    rnd = random.Random()
    min_age, max_age = 1, 30

    for _ in range(3):
        t1 = Tree(TreeType.apple)
        t1.render(rnd.randint(min_age, max_age))

    for _ in range(4):
        t1 = Tree(TreeType.cherry)
        t1.render(rnd.randint(min_age, max_age))

    for _ in range(5):
        t1 = Tree(TreeType.peach)
        t1.render(rnd.randint(min_age, max_age))


if __name__ == '__main__':
    main()
