# tag::BINGO[]

import random


# Illustrates callable instances
class BingoCage:

    def __init__(self, items):
        self._items = list(items)  # <1>
        random.shuffle(self._items)  # <2>

    def pick(self):  # <3>
        try:
            return self._items.pop()
        except IndexError as e:
            raise LookupError("pick from empty BingoCage") from e

    def __call__(self):  # <5>
        return self.pick()


if __name__ == "__main__":
    bingo = BingoCage(range(3))
    print(bingo.pick())
    print(bingo.pick())
