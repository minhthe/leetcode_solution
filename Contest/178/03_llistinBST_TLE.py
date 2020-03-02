'''
https://leetcode.com/problems/linked-list-in-binary-tree
'''

class Solution(object):
	def isSubPath(self, head, root):
		i =  0
		tmp = head
		arr = []
		while(tmp):
			arr.append(tmp.val)
			tmp = tmp.next
		n = len(arr)
		def f(arr, head, root, p, n):
			if (p == n): return True
			if(root.val == arr[p]):
				if(p == n-1):
					return True
				
				if(root.left):
					if f(arr, head, root.left, p+1, n) == True: return True

				if(root.right) :
					if  f(arr, head, root.right, p+1, n) == True: return True

			else:
				p = 0
				if(root.val == arr[0]):
					if f(arr, head, root, p, n) == True: return True
				if(root.left):
					if  f(arr, head, root.left, p, n) == True: return True
					
				if(root.right) :
					if f(arr, head, root.right, p, n) == True:  return True
			return False
		return f(arr, head, root, 0, n)