class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        m=[]
        for i in range(len(words)):
            for j in words[i]:
                if j==x:
                    m.append(i)
        return list(set(m))
S=Solution()
words = ["leet","code"]
x = "e"
print(S.findWordsContaining(words,x))               

        