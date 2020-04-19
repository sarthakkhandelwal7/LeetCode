class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.helper(ans, s, 4, [])
        print(ans)
        return ['.'.join(x) for x in ans]

    def helper(self, ans, s, k, temp):
        print(f'k: {k}\ns: {s}\ntemp: {temp}')
        if len(s) > k * 3:
            return

        if k == 0:
            print(temp)
            ans.append(temp[:])

        else:
            for i in range(min(3, len(s) - k + 1)):
                print(f'len of s: {len(s)}\ts: {s}\t{len(s) - k + 1}')
                print(f'i: {i}')
                print()
                if i == 2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
                    print('In if case\n')
                    continue
                self.helper(ans, s[i + 1:], k - 1, temp + [s[:i + 1]])


if __name__ == '__main__':
    print(Solution().restoreIpAddresses("25525511135"))