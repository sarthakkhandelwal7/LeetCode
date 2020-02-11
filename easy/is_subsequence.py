class Solution:
    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        if len(s) is 0 or len(t) is 0:
            return False

        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        print(i)
        if i == len(s):
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().isSubsequence("abc", "ahbgdc"))
