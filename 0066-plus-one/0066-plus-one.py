class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=len(digits)-1
        n=0
        for i in range(len(digits)):
            n+=(digits[i]*(10**c))
            c-=1
        n+=1
        a=[]
        c=len(str(n))-1
        for i in range(len(str(n))):
            a.append(n//(10**c))
            n-=(n//(10**c))*(10**c)
            c-=1
        return a
        
        
                
            
        
            

s=Solution()
digits = [1,2,3]
print(s.plusOne(digits))


        