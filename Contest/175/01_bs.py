'''
https://leetcode.com/problems/check-if-n-and-its-double-exist/

[10,2,5,3]
[0,0]
[3,1,7,11]
[-20,8,-6,-14,0,-19,14,4]
[-2,0,10,-19,4,6,-8]

'''
class Solution(object):
	def checkIfExist(self, arr):
	
		arr_sorted = sorted(arr)
		n = len(arr)
		if(n<=1): return False
		def findBS(x, l , r, a):
			while(l<=r):
				mid = int(r + (l -r)/2)
				if(a[mid] == x):
					return True
				elif(a[mid] > x):
					r = mid - 1 
				else:
					l = mid + 1 
			return False
		for i in range(n-1):
			l, r = i+1, n-1
			if(arr_sorted[i] <= 0 and arr_sorted[i]&1==1):
				continue
			if(arr_sorted[i] <= 0 and arr_sorted[i]&1==0):
				x = arr_sorted[i] /2 
			elif(arr_sorted[i] > 0):
				x = arr_sorted[i] * 2 
			if(findBS(x, l, r, arr_sorted) ):
				return True
		return False