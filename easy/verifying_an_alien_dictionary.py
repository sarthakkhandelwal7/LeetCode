class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        sequence = dict()
        for i, char in enumerate(order):
            sequence[char] = i

        for i in range(len(words) - 1):

            word_1 = words[i]
            word_2 = words[i+1]
            j = k = 0

            while len(word_1) - 1 != j and len(word_2) - 1 != k and sequence[word_1[j]] == sequence[word_2[k]]:
                j += 1
                k += 1

            if sequence[word_1[j]] < sequence[word_2[k]]:
                continue

            if sequence[word_1[j]] == sequence[word_2[k]] and len(word_2) - 1 == k or sequence[word_1[j]] > sequence[word_2[k]]:
                return False

        return True


if __name__ == '__main__':
    print(Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
    print(Solution().isAlienSorted(["world","row"], "worldabcefghijkmnpqstuvxyz"))