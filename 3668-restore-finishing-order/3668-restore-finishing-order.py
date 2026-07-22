class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        o=[]
        for i in order:
            if i in friends:
                o.append(i)
        return o
s=Solution()
order = [3,1,2,5,4]
friends = [1,3,4]
print(s.recoverOrder(order,friends))