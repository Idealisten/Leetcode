class Solution:
    def mySqrt(self, x: int):
        for a in range(0, x+1):
            square = a * a
            if square == x:
                return a
            elif square > x:
                return a-1

