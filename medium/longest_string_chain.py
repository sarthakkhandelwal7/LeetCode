from collections import defaultdict


class Solution:
    def longestStrChain(self, words) -> int:
        sub_chains = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                sub_chains[word[:i]+word[i+1:]].append(word)

        chains = list()

        def helper(chain):

            if chain[-1] not in sub_chains:
                chains.append(chain.copy())
                return

            for word in sub_chains[chain[-1]]:
                chain.append(word)
                helper(chain)

                chain.pop()

        for word in words:
            helper([word])

        return max([len(chain) for chain in chains])


if __name__ == '__main__':
    print(Solution().longestStrChain(["a","b","ba","bca","bda","bdca"]))
