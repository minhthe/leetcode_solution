'''
https://leetcode.com/problems/target-sum/

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
'''
class Solution(object):
    def findTargetSumWays(self, nums, S): 
        
        n , memo, p = len(nums), {}, 0
        
        def f(p,S, memo, nums):
            
            if((p,S) in memo): return memo[(p,S)]
            if(p == n and S == 0):return 1            
            if(p == n and S != 0): return 0
            
            pos =  f(p + 1,S - nums[p], memo, nums)          
            neg =  f(p + 1, S + nums[p], memo, nums)            
            memo[(p,S)] = pos + neg
            
            return memo[(p,S)]
        return f(p,S, memo, nums)
        