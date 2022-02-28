#   记忆递归
memo = [0, 1, 2]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n > 2:
            memo.extend([0]*(n-2))
        if memo[n] != 0:
            return memo[n]
        else:
            memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return memo[n]


s = Solution()
print(s.climbStairs(3))



