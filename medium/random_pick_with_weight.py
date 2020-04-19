import bisect
import itertools
import random


class Solution:

    def __init__(self, w):
        self.w = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        # ex [1, 2, 5, 12]
        # accumulate list = [1, 3, 8, 20]
        # 1-3 has small range than 8 - 20 so probability of picking 12 is more than 1 or 2
        return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))
