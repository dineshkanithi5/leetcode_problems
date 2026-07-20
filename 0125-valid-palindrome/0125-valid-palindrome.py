import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        s=s.lower()
        l=list(string.ascii_lowercase)+list(string.digits)
        for i in range(len(s)):
            if s[i] in l:
                a+=s[i]
        m=a[::-1]
        if a==m:
            return True
        else:
            return False
S=Solution()
s = "A man, a plan, a canal: Panama"
print(S.isPalindrome(s))


        