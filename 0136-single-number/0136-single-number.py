class Solution:
    def singleNumber(self, nums):
        return  2*(sum(set(nums)))-sum(nums)
nums=[2,2,1]
p1=Solution()
p1.singleNumber(nums)

        