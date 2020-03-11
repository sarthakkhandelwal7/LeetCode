from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        for i in strs:
            sum = 0
            for char in i:
                sum += ord(char) - ord('a')

            anagrams[sum].append(i)
        return [i for i in anagrams.values()]


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
