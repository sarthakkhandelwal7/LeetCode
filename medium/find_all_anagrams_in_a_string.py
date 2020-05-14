class Solution:
    def findAnagrams(self, s: str, p: str):
        ans = list()
        anagram = [0] * 26
        count = [0] * 26
        m, n = len(s), len(p)
        if m < n:
            return []
        for i, ch in enumerate(p):
            anagram[ord(ch) - ord('a')] += 1
            count[ord(s[i]) - ord('a')] += 1

        for i in range(m):

            if count == anagram:
                ans.append(i)

            if i + n >= m:
                break

            count[ord(s[i]) - ord('a')] -= 1
            count[ord(s[i + n]) - ord('a')] += 1
        return ans
