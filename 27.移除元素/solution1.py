class Solution:
    def removeElement(self, nums, val):
        c = 0
        for num in nums:
            if num == val:
                c = c + 1
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == val:
                while nums[j] == val and i < j:
                    j = j - 1
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
            i = i + 1
        print(nums)
        return len(nums) - c


s = Solution()
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))



