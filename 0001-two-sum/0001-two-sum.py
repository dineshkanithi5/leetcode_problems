class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx=[]
        for i,num in enumerate(nums):
            idx.append((num,i))
        idx.sort()
        p1=0
        p2=len(nums)-1
        while(p1<p2):
            if idx[p1][0]+idx[p2][0]==target:
                return idx[p1][1],idx[p2][1]
            elif idx[p1][0]+idx[p2][0]>target:
                p2-=1
            else:
                p1+=1
nums=[2,7,11,15]
target=9                
S=Solution()
print(S.twoSum(nums,target)) 

