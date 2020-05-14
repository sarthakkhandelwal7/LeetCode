class Solution(object):
    def consecutiveNumbersSum(self, N):
        count = 0
        n = 1
        while n*(n+1)/2 < N:
            if (N - n*(n+1)/2) % n == 0:
                count += 1

            n += 1

        return count + 1


if __name__ == '__main__':
    print(Solution().consecutiveNumbersSum(15))