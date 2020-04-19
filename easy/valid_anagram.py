from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = Counter(s)
        t_counts = Counter(t)

        if len(s) != len(t):
            return False

        for k, v in s_counts.items():
            if t_counts[k] != v:
                return False
        return True
