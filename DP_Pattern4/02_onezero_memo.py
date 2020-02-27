'''
https://leetcode.com/problems/ones-and-zeroes/

'''
class Solution(object):
    def findMaxForm(self, strs, m, n):
        
        def f(p, strs, m ,n, memo):
            if((p,m,n) in memo):
                return memo[(p,m,n)]
            if(p == len(strs)):
                return 0
            num_1 = strs[p].count('1')
            num_0 = strs[p].count('0')
            k = 0
        
            if(m >=num_0 and n>= num_1):
                pick = 1 + f(p+1, strs, m - num_0, n-num_1, memo)
                not_pick = f(p+1, strs, m, n, memo)
                k = max(pick, not_pick) 
            else:
                not_pick = f(p+1, strs, m, n, memo)
                k = not_pick
            memo[(p,m, n)] = k
            return k 
        p = 0 
        memo = {}
        return f(p, strs, m ,n, memo )
        