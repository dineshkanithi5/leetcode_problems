class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        a=list(s)
        b=list(t)
        a.sort()
        b.sort()
        c=0
        if a==b:
            return True
        return False
        
s="anagram"
t="nagaram"
S=Solution()
print(S.isAnagram(s,t))

                
        