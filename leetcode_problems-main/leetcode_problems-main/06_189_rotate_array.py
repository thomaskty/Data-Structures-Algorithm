# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# 
# Example 1:
# 
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
# 
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#  
# 
# Constraints:
# 
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
#  
# 
# Follow up:
# 
# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

def reverse(ar,k):
    k = k%len(ar) 
    
    i,j = 0,len(ar)-1 
    while i<j:
        ar[i],ar[j] = ar[j],ar[i]
        i+=1;j-=1
        
    i,j = 0,k-1 
    while i<j:
        ar[i],ar[j] = ar[j],ar[i]
        i+=1;j-=1
        
    i,j = k,len(ar)-1 
    while i<j:
        ar[i],ar[j] = ar[j],ar[i]
        i+=1;j-=1

array = [2,3,4,2,1,84,94,85]
reverse(array,2)
print(array)

