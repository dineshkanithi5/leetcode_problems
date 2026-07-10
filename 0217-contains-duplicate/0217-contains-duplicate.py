class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a={}
        for i in range(len(nums)):
            if nums[i] in a:
                return True
            else:
                a[nums[i]]=1
        return False
nums=[1,2,3,4]
S=Solution()
res=S.containsDuplicate(nums)
print(res)