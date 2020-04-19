class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_pad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if '1' in digits or not digits:
            return []
        ans = ['']

        for digit in digits:
            level_length = len(ans)
            while level_length:
                for char in number_pad[digit]:
                    ans.append(ans[0] + char)
                ans = ans[1:]
                level_length -= 1
        return ans
