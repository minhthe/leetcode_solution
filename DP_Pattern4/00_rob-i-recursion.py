'''
https://leetcode.com/problems/house-robber/

2 things need to indetify with this clasic recursive problem:
1) indentiy the base problem -> build the base condtion
2) the formula.

***Practice compelixty:
A time complexity
1) C units operations on the function f = '==' and "+", max  -> should build this function with top - down conrespond with function below
-> T(n) = C + T(n-1) + T(n-2)  
    T(n-1) ~~ T(n-2)
-> T(n) = C + 2T(n-2) 
-> T(n) = C + 2{2T(n-4) + C} = 4T(n-4) + 3C
...
https://youtu.be/pqivnzmSbq4?list=PL2_aWCzGMAwLz3g66WrxFGSXvSsvyfzCO

-> T(n) = 2^n (upper bound) -> exponential time algorithm


'''
class Solution(object):
	def rob(self, nums):
		m = len(nums)
		if m == 0 : return 0
		memo = {}		
		def f(m, nums, memo):
			if m in memo: return memo[m]
			if(m == 0)		:
				memo[m] = nums[0]	
				return memo[m]
			if(m == 1):
				memo[m] = max(nums[0],nums[1])
				return memo[m]
			if(m == 2):
				memo[m]= max(nums[0]+nums[2],nums[1])
				return memo[m]
			else:
				a = nums[m] + f(m-2, nums, memo)
				b = nums[m-1] + f(m-3, nums, memo)
				memo[m] = max(a,b)
				return memo[m]
		return f(m -1, nums, memo)