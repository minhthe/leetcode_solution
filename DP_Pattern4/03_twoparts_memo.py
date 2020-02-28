'''
https://leetcode.com/problems/partition-equal-subset-sum
'''
class Solution(object):
	def canPartition(self, nums):
		s = sum(nums)
		if s&1: return False
		s = s/ 2
		p = 0
		def f(nums, n , s, p, memo):
			if( (p,s) in memo ): return memo[(p,s)]
			if(p == n):
				return False
			if(s == 0):
				memo[(p,s)] = True
				return True 
			if(s >= nums[p]):
				pick = f(nums, n, s - nums[p], p+1, memo)
				if pick == True: return True
				not_pick = f(nums, n, s, p+1, memo)
				if not_pick == True: return True
			else:
				not_pick = f(nums, n, s, p+1, memo)
				if not_pick == True: return True
			memo[(p,s)] = False
			return memo[(p,s)]
		memo = {}		
		return f(nums, len(nums), s, p, memo)