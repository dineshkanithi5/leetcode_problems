class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List [int]:
        m=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                m.append(nums1[i])
        return list(set(m))
nums1=[1,2,2,1] 
nums2=[2,2]
S=Solution()
print(S.intersection(nums1,nums2))


        