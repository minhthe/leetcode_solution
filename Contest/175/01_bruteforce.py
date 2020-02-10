''''
https://leetcode.com/problems/check-if-n-and-its-double-exist/

***operation ^:
same  = 0 
diff = 1
''''

class Solution(object):
    def checkIfExist(self, arr):
		for i in range(len(arr)):
			for j in range(len(arr)):
				if(i ^ j and arr[i] * 2 == arr[j] ):
					return True
		return False