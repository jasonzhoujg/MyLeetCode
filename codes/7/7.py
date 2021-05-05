class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:x = int(str(abs(x))[::-1])
        else: x = -int(str(abs(x))[::-1])
        if x>pow(2,31)-1 or x< -pow(2,31):return 0
        return x
