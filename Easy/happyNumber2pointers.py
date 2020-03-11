'''
https://leetcode.com/problems/happy-number/

*** edge case: 10 -> so add condtion first != 1

'''
class Solution:
    def isHappy(self, n: int) -> bool:
        first = n
        second = n
        def generate(n):
            tmp = [int(x) *int(x) for x in list(str(n))]
            return sum(tmp)	
            
        while(first != 1 and second != 1):
            first = generate(first)
            second = generate(generate(second))
            if(first == second and first !=1)    : return False
        return True