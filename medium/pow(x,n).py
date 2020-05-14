class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        start = i = curr = total = 0
        for g, c in zip(gas, cost):
            total += g-c
            curr += g-c
            if curr < 0:
                start = i+1
                curr = g-c
            i += 1
        return start
