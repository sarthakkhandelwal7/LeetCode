class Solution:
    def maxSatisfied(self, customers, grumpy, X: int) -> int:
        happy_customers = 0
        total = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total += customers[i]
                customers[i] = 0
        print(customers)
        best = 0
        curr_best = 0
        for i in range(len(customers)):
            curr_best += customers[i]
            if i >= X:
                curr_best -= customers[i - X]

            best = max(curr_best, best)
        return best + total


if __name__ == '__main__':
    print(Solution().maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))
