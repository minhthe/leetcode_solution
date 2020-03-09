'''
https://leetcode.com/problems/last-stone-weight/

###notes:

the heapq._heapq_max(stones) -> NOT maintain the heap-max when pop 
ex: [10,4,2,10] 	-> heapq._heapify_max(stones)
'''
import heapq
class Solution(object):
	def lastStoneWeight(self, stones):
		stones = [-x for x in stones]
		heapq.heapify(stones)
		while(len(stones) >= 2):
			tmp = abs( heapq.heappop(stones)-   heapq.heappop(stones)  )
			if(tmp): heapq.heappush(stones, -tmp)
		return abs(heapq.heappop(stones)) if len(stones) else 0