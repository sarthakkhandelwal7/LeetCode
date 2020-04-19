from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.size = 0

    def get(self, key: int) -> int:

        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
            self.size -= 1

        if self.size == self.capacity and key not in self.cache:
            self.cache.popitem(last=False)
            self.size -= 1

        self.size += 1
        self.cache[key] = value


if __name__ == '__main__':

    ans = []

    obj = LRUCache(2)
    ans.append('null')
    obj.put(1, 1)
    ans.append('null')
    obj.put(2, 2)
    ans.append('null')
    ans.append(obj.get(1))
    obj.put(3, 3)
    ans.append('null')
    ans.append(obj.get(2))
    obj.put(4, 4)
    ans.append('null')
    ans.append(obj.get(1))
    ans.append(obj.get(3))
    ans.append(obj.get(4))
    print(ans)
