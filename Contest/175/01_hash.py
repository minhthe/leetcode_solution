'''
https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution(object):
    def checkIfExist(self, arr):
		set_arr = set(arr)
		if(arr.count(0) > 1): return True 
		for item in set_arr:
			if(item*2 in set_arr):
				return True 
		return False
''''

class Solution(object):
    def checkIfExist(self, arr):
		set_arr = set(arr) - {0}
		if(arr.count(0) > 1): return True 
		for item in set_arr:
			if(item*2 in set_arr):
				return True 
		return False