class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f={}
        for i in nums:
            if i not in f:
                f[i]=1
            else:
                f[i]+=1
            if f[i]>len(nums)//2:
                return i
        return nums[0]
                
       
         
    
nums=[2,2,1,1,1,2,2]
s=Solution()
print(s.majorityElement(nums))
