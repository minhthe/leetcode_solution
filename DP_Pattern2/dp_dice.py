'''
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
***formular
	k[i][j] = k[i][j-1]  + k[i-1][j-1]
wrong with this case: -> expect is 18 (with d=3, f=5,t=7 is Right)
3
5
8
[[0, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 1, 2, 3, 4, 5, 4, 3], [0, 0, 0, 1, 3, 6, 10, 15, 19]]

'''
class Solution(object):
	def numRollsToTarget(self, d, f, target):
		t = target
		k = [[0 for i in range(t+1)] for j in range(d)]
		for i in range(1, t+1):
			if(i<=f):k[0][i] = 1
		# print(k)
		cnt = 0
		pos = -1
		for i in range(1,d):
			for j in range(1,t+1):
				if( j== 1):
					k[i][j] = 0
				else:
					if(j!= 1 and k[i-1][j-1]==0):
						if pos!=-1 : 
							tmp = tmp -1
							print(tmp)
							k[i][j] = k[i][tmp] if tmp >= 0 else 0
						else:
							pos = j - 2                        
							k[i][j] = k[i][pos]
							tmp = pos
					else:
						k[i][j] = k[i][j-1]  + k[i-1][j-1]
		print(k)
		return k[d-1][t] %int(1e9+7)