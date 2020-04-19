from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        for i in strs:
            count = [0]*26
            for char in i:
                count[ord(char) - ord('a')] += 1
            anagrams[tuple(count)].append(i)
        return [i for i in anagrams.values()]


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
