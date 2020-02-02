'''
https://leetcode.com/problems/add-digits/s

***practice complexity base on :
https://youtu.be/pqivnzmSbq4?list=PL2_aWCzGMAwLz3g66WrxFGSXvSsvyfzCO

***Complexity:

i) Time complexity for this recursion: 

1) loop length of Num + sum operation -> transfer to list -> 2 * O(n)  
2) base condtion: if len(s) == 1
    -> when len(s) == 1? -> number of list s is 1 
    -> sum of list s is from [0, 9] -> when ???
    ex: 999999999..9-> 9*10^9 = 9000000000..0-> 9
    
    the step of leng(s)  =1 is very short, just 2 step like above ex
-> so the time complexity is just O(n) -> tranfer to the list 

ii) Space complexity: is about unit of stack of the memory = unit of function is loaded on the memory -> base on ex just about 3 function-> so O(1)
and declare the list s -> which will take O(n) space, which n is the length of Num
'''
def addNum(num):
    s = list([int(x) for x in str(num)])
    if(len(s) == 1):
        return s[0]
    return addNum(sum(s))
class Solution(object):
    def addDigits(self, num):
        return addNum(num)
'''
#### iteration function:

class Solution(object):
    def addDigits(self, num):
        tmp = num
        while(True):
            
            l = list([ int(x) for x in str(tmp) ])
            if(len(l) == 1  ):
                return sum(l)
            else:
                tmp = sum(l)
#or this:
class Solution(object):
    def addDigits(self, num):
        tmp = num
        while(len(list([ int(x) for x in str(tmp) ]))!= 1):
                tmp = sum(list([ int(x) for x in str(tmp) ]))
        return sum(list([ int(x) for x in str(tmp) ]))                
                        
        
'''        