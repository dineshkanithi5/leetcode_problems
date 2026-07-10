class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,n in enumerate(nums):
            if target-nums[i] not in seen:
                seen[n]=i
            elif target-nums[i] in seen:
                return seen[target-nums[i]],i



nums=[2,7,11,15]
target=9                
S=Solution()
print(S.twoSum(nums,target)) 

