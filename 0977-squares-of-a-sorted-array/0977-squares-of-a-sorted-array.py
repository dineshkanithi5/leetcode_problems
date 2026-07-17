class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=(nums[i])**2
        nums.sort()
        return nums
s=Solution()
nums = [-7,-3,2,3,11]
print(s.sortedSquares(nums))
        