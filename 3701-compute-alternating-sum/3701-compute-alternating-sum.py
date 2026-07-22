class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        m=0
        for i in range(len(nums)):
            if i%2==0:
                m+=nums[i]
            else:
                m-=nums[i]
        return m
s=Solution()
nums = [1,3,5,7]
print(s.alternatingSum(nums))

        