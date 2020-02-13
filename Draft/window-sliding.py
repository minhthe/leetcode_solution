'''
for debug understand dequeue which is only take O(1) time compleixty 
-> LRU, pratice more slidewodown , 2 pointer

https://leetcode.com/problems/sliding-window-maximum/discuss/500582/Python-solution-using-deque-with-two-pointer-templates



'''

import collections
if __name__ == '__main__':
    
    def maxSlidingWindow( nums,k):
        
        begin = 0
        q = collections.deque([])
        output = []
        for end in range(len(nums)):
            #######
			## This make sures that the leftmost element must be the largest
			## Note that we are not adding the element but its index
            while q and nums[end] > nums[q[-1]]:
                q.pop()
			#######
			## This makes sure every element will be added into queue
            q.append(end)
            
			## This makes sure that for every sliding window
			## the leftmost element will be removed from the queue 
			#### if it is not within the sliding window
            while end - begin + 1 > k:
                begin +=1
                if q[0] < begin:
                    print('herere')
                    q.popleft()
            
			### for every sliding window
			### we add the leftmost element (maxium within the sliding window) into the output
            if end - begin + 1 == k:
                output.append(nums[q[0]])
                
        return output
    nums = [5,3,4]
    k = 1
    rst = maxSlidingWindow(nums, k)
    print(rst)