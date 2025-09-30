# ## Maximum sub-array - Question 4
# Question:
# Write a Python function to find the maximum sum of a contiguous subarray 
# from a given list of integers. 
# The function should implement an efficient algorithm with O(n) time complexity 
# and return the maximum sum.
# ```python
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(max_subarray_value(nums))  # Output: 6
# ```
# Constraints:
# * The input list may contain both positive and negative integers.
# * The function should handle edge cases like single-element arrays or 
# all-negative numbers efficiently.
# 

array = [-2,1,-3,4,-1,2,1,-5,4]

def max_subarray_value(nums):
    maxSub = nums[0]
    curSum = 0 
    for n in nums:
        if curSum<0:
            curSum=0
        curSum +=n 
        maxSub = max(maxSub,curSum)
    return maxSub
    
max_subarray_value(array)

