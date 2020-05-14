class Solution:
    def rangeBitwiseAnd(self, a: int, b: int) -> int:
        # -b is the 2's complement of b
        # when do bitwise or with b we
        # get LSB and we subtract that from b
        while a < b:
            b -= (b & -b)
        return b
