class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            elif nums[i]>target:
                return i
        return len(nums)
s=Solution()
nums = [1,3,5,6]
target = 5
print(s.searchInsert(nums,target))