class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        c=0
        for i in range(n-1,-1,-1):
            if nums[i]==val:
                nums.remove(val)
        return len(nums)
s=Solution()
nums=[3,2,2,3]
val=3
print(s.removeElement(nums,val))
        