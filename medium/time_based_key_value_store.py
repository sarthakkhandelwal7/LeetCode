from collections import defaultdict
from bisect import bisect


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        index = bisect(self.store[key], ('', timestamp))
        return self.store[key][index+1][0]



