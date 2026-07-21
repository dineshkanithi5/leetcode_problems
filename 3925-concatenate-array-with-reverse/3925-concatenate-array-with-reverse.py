class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums+nums[::-1]
s=Solution()
nums = [1,2,3]
print(s.concatWithReverse(nums))
        