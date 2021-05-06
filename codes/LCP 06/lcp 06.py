class Solution:
    def minCount(self, coins: List[int]) -> int:
        n = 0
        for i in range(len(coins)):n+= -(-coins[i]//2)
        return n
