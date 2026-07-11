class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List [int]:
        a={}
        b={}

        for i in nums1:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in nums2:
            if i in b:
                b[i]+=1
            else:
                b[i]=1
        m=[]
        for i in a:
            if i in b:
                m.append(i)
        return m
                
        
            


 
        

nums1=[1,2,2,1] 
nums2=[2,2]
S=Solution()
print(S.intersection(nums1,nums2))


        