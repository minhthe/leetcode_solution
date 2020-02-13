'''
https://leetcode.com/problems/squares-of-a-sorted-array/

time complextiy : O(n)
space complextiy : O(n)
'''
class Solution(object):
    def sortedSquares(self, A):
        n = len(A)
        if n == 0 : return []
        rst = [0] * (n)
        i , j = 0, n -1 
        k = n-1
        while(i<=j):
            if(abs(A[i]) > A[j] ):
                rst[k] = A[i] * A[i]
                i +=1 
                k-=1
            else:
                rst[k] = A[j] * A[j]
                k-=1
                j -=1
        return rst
      
        