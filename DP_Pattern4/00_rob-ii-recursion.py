
'''
https://leetcode.com/problems/house-robber-ii/
this problem hard to find the base condition:

the base conditon even with 5 elements : ex : [2,7,9,3,1]

***tet case
[2,3,2]
[1,2,3,1]
[2,7,9,3,1] -> base condion
[1,1,3,6,7,10,7,1,8,5,9,1,4,4,3] -> wrong as pass start by value, make wrong value


'''
class Solution(object):
	def rob(self, nums):
		pos = len(nums) - 1 
		start = 0 
		if pos == -1 : return 0
		memo = {}
		def f(start, pos, nums, memo):
			if (start,pos) in memo:
				return memo[(start,pos)]
			if start > pos : return 0
			if(pos == start):
				memo[(start,pos)] =  nums[pos]
				return memo[(start,pos)]
			if(pos - start == 1):
				memo[(start,pos)]= max(nums[pos], nums[start])
				return memo[(start,pos)]
			if (pos == len(nums) -1):
				a = nums[pos] + f(1, pos -2, nums , memo)
			else:
				a = nums[pos] + f(start, pos -2, nums , memo)
			b  = nums[pos -1] + f(start, pos -3, nums, memo)
			c =  nums[pos -2] + f(start, pos -4, nums, memo)
			memo[(start,pos)] = max(a,b,c)
			return memo[(start,pos)]
		ans = f(start, pos, nums, memo)
		return ans