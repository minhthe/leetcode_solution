'''

Recursion with memo-> the resut will be return 15
but still don't test all test case
ex: if W ==0: memo[pos] = 0 -> the result wil be 14



'''
class Item:
	def __init__(self, profit, weight):
		self.profit= profit
		self.weight = weight 
if __name__ == '__main__':
	items= [Item(1,1 ),Item(2,1 ),Item(2,2 ),Item(4,6),Item(10,4 )]
	W = 10
	def f(items, pos , W, rst, memo):
		if(pos in memo): return memo[pos]
		if(W ==0):
			return 0
		if(pos == 0 ):
			if (W >= items[0].weight):			
				memo[pos] = items[0].profit
				rst.append(items[0])
				return memo[pos]
			else:
				memo[pos] = 0
				return 0
		if(W - items[pos].weight) < 0 :
			memo[pos] = f(items, pos-1, W , rst, memo )
			return memo[pos]
		else:
			pick = items[pos].profit + f(items, pos-1, W - items[pos].weight, rst, memo ) 

			notpick = f(items, pos-1, W , rst, memo ) 
			memo[pos] = max(pick, notpick)
			if pick > notpick: rst.append(items[pos])
 			#else: rst.append(notpick)
			return memo[pos]
		
	rst = []			
	m = len(items)
	memo = {}
	print(f(items,m -1 , W, rst, memo))
	for item in rst:
		print(item.weight, '--', item.profit)