class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for x in nums:
            if x in freq:
                freq[x]=freq[x]+1
            else:
                freq[x]=1
        for x in freq:
            if freq[x]==1:
                return x
S=Solution()
print(S.singleNumber)        