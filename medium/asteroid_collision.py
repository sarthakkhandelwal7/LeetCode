class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for asteroid in asteroids[::-1]:
            check_flag = False
            while stack and stack[-1] < 0 and asteroid > 0:

                temp = stack.pop()
                if abs(temp) < asteroid:
                    continue

                elif abs(temp) == asteroid:
                    check_flag = True
                    break

                else:
                    asteroid = temp

            if not check_flag:
                stack.append(asteroid)

        return stack[::-1]


if __name__ == '__main__':
    print(Solution().asteroidCollision([5, 10, -5]))
    print(Solution().asteroidCollision([10, 2, -5]))
    print(Solution().asteroidCollision([-2, -1, 1, 2]))
    print(Solution().asteroidCollision([5, 10, 0, -5]))
    print(Solution().asteroidCollision([5, 10, 7, 3, -6, -8, 8, -4, 1, -2, -5]))
    print(Solution().asteroidCollision([8, -8]))
