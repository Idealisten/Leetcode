#   二分查找
class Solution:
    def mySqrt(self, x: int):
        if x == 0:
            return 0
        else:
            left = 1
            right = x
            while left <= right:
                mid = (left + right) // 2
                square = mid * mid
                square2 = (mid + 1) * (mid + 1)
                if square == x or ((square < x)
                                   and square2 > x):
                    return mid
                else:
                    if square > x:
                        right = mid - 1
                    else:
                        left = mid + 1


s = Solution()
print(s.mySqrt(4))
