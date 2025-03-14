## Three sum : Question 3
# Question:
# Write a Python function to find all unique triplets in a given list of integers 
# that sum up to a given target value. Each triplet should be sorted in ascending order, 
# and the function should ensure that no duplicate triplets appear in the output. 
# The solution should run in O(n²) time complexity using sorting and the two-pointer technique.
# ```python
# ar = [-3, -3, -3, -3, 6, 5, 5, 4, 3, 2, 1]
# target = 0
# print(three_sum(ar, target))
# # Output: [[-3, 1, 2], [-3, -3, 6]]
# ```
# Constraints:
#  * The input list may contain both positive and negative integers.
#  * The function should return unique triplets (no duplicate sets).
#  * The order of triplets in the result does not matter.
#  * The function should handle cases where no triplets exist.

def three_sum(nums,target):
    res = [] 
    nums.sort() 
    for i,num in enumerate(nums): 
        # i is the iteration pointer 
        if ((i>0) & (num==nums[i-1])):
            continue
        # inside i we have two other pointers
        # total three distinct pointers 
        start,end = i+1,len(nums)-1 
        while start<end:
            _sum = num+nums[start]+nums[end]
            if _sum<target:
                start+=1
            elif _sum>target:
                end-=1 
            else:
                res.append((num,nums[start],nums[end]))
                start +=1
                while ((start<end) & (nums[start]==nums[start-1])):
                    start+=1 
    return res 
