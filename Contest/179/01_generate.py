'''
https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
'''
class Solution:
    def generateTheString(self, n: int) -> str:
        
        rst = ['a' for i in range(n)]            
        if n & 1: 
            return ''.join(rst)
        else:
            rst[0] = 'b'
            return ''.join(rst)