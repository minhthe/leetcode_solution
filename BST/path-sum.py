'''
https://leetcode.com/problems/path-sum/
AC in 22 minutes

***approach: using recursive function


***edge case:
[] 0 -> False
[1,2] 0 -> add condition if root is None in the "check" function

***next:
Practice with dfs and bfs.
'''
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
def check(root, k, sum):
	if(root is None):
		return
	if(root.left == None and root.right==None):
		
		return k + root.val == sum

	if(check(root.left, k + root.val, sum)):
			return True

	if(check(root.right, k + root.val, sum)):
			return True
	
	
class Solution(object):
	def hasPathSum(self, root, sum):
		if root is None and sum == 0:
			return False
		if root is None and sum != 0:
			return False
		if(check(root, 0, sum)):
			return True
		else:
			return False