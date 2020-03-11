'''
https://leetcode.com/problems/decode-ways/
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        arr = list(s)
        n = len(arr)
        start, memo = 0, {}
        def condition(start, end, arr, memo):
            
            if (end == start + 1 and  int( ''.join(arr[start:end]) ) == 0 ): 
                    return False
            if( end == start + 2 and ( int(''.join(arr[start: start +1])) == 0 or int(''.join(arr[start: start +2])) > 26 )):
                    
                    return False
            return True
        def  f(start,end, arr, memo):
            if ((start, end) in memo): return memo[(start, end)]
            
            if(end > len(arr)): return 0 
            if(end == len(arr)): 
                if(condition(start, end, arr, memo)): 
                    memo[(start, end)] = 1
                    return 1
                else: 
                    memo[(start, end)] = 0
                    return 0
            if(condition(start, end, arr, memo)):
                memo[(start, end)] = f(end,end + 1 , arr, memo) + f(end,end +2, arr, memo)
                return  memo[(start, end)] 
            else:
                memo[(start, end)] = 0
                return 0
                
            
        return f(start, start + 1, arr, memo) +  f(start, start + 2, arr, memo)
        
        
        