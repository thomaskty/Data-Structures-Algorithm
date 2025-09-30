## Maximum Subarray - Question 5 
# Question:
# Modify the function from Part 1 to return the actual subarray that produces the maximum sum, 
# in addition to the sum itself. The function should still run in O(n) time complexity 
# and return both the maximum sum and the subarray responsible for it.
# ```python
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(max_subarray_with_indices(nums))  
# # Output: (6, [4, -1, 2, 1])
# ```
# Constraints:
# 
# * The input list may contain both positive and negative integers.
# * If there are multiple subarrays with the same maximum sum, return the first one found.
# * The function should handle cases like a single-element list or all-negative numbers efficiently.

def max_subarray_with_indices(nums):
    maxSub = nums[0]  # Stores the max sum found
    curSum = 0  # Tracks current subarray sum
    
    start = 0  # Start index of the current subarray
    best_start, best_end = 0, 0  # Best subarray indices
    
    for i, n in enumerate(nums):
        if curSum < 0:
            curSum = 0
            start = i  # Reset the start index
        
        curSum += n
        
        if curSum > maxSub:
            maxSub = curSum
            best_start, best_end = start, i  # Update best indices
    
    return maxSub, nums[best_start:best_end+1]  # Return max sum and subarray

# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_with_indices(nums)
print(result)  # Output: (6, [4, -1, 2, 1])



