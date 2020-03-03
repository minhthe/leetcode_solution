'''
https://leetcode.com/problems/last-stone-weight-ii/

S = S1 + S2
diff = S1 - S2 -> S1 = diff + S2 
-> S = 2*S2 + diff -> diff = S - 2*S2 
-> min diff -> Max S2
'''
class Solution(object):
	def lastStoneWeightII(self, stones):
		n = len(stones)
		s = sum(stones) 
		p = 0
		def f(p, s, stones, memo):
			if(p == n): return 0
			if((p,s) in memo): return memo[(p,s)]
			if(s >= stones[p]):
				pick = stones[p] + f(p +1, s - stones[p], stones, memo)
				not_pick = f(p+1, s, stones, memo)
				memo[(p,s)] = max(pick, not_pick)
			else:
				memo[(p,s)] = f(p+1, s, stones, memo)
			return memo[(p,s)]
			
		memo = {}
		
		s2 = f(p, s//2, stones, memo)
		return s - 2* s2