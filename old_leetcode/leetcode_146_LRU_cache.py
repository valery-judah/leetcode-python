from collections import OrderedDict


# todo add tests
class LRUCache:

    def __init__(self, capacity: int):
        self.items = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.items:
            self.items.move_to_end(key)
            return self.items[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.items:
            if len(self.items) == self.capacity:
                self.items.popitem(last=False)
        else:
            del self.items[key]
        self.items[key] = value

    def __str__(self) -> str:
        return self.items.__str__()


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 12)
    print(cache)

    cache.get(1)
    print(cache)

    cache.put(3, 20)
    print(cache)
# todo: use dict, then orderedDict, add tests
