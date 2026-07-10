class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s=set()
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                return True
        return False
S=Solution()
nums=[1,2,3.4]
res=S.containsDuplicate(nums)
print(res)