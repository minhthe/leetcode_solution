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
		def f(s, pos, nums, arr, m, n, memo):
			if(pos in memo):
				return memo[pos]
			if (n==0): return 0 
			if (n ==1) : 
				memo[pos] = arr[0]
				return memo[pos]
			if (n == 2): 
				memo[pos] = max(arr)
				return memo[pos]
			if (n == 3):
				memo[pos] = max(arr[0] + arr[2], arr[1] )
				return memo[pos] 
			a = arr[0]  + f(s, pos + 2, nums, nums[pos + 2:], m, len( nums[pos + 2:]), memo)
			b = arr[1]  + f(s , pos + 3, nums, nums[pos + 3:], m, len( nums[pos + 3:]), memo)
			memo[pos] = max(a, b)
			return memo[pos]
		s, pos, nums, arr, m, n , memo = 0, 0, nums, nums, len(nums), len(nums), {}
		return f(s, pos, nums, arr, m, n, memo)