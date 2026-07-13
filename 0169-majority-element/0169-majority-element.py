class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       
        m=list(set(nums))
        for i in m:
            c=nums.count(i)
            if c>len(nums)//2:
                return i       
    
nums=[2,2,1,1,1,2,2]
s=Solution()
print(s.majorityElement(nums))
