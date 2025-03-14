# # question 9 : remove duplicates and return the number of unique elements 
# 
# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.
# 
# Consider the number of unique elements of nums to be k, to get accepted,
# you need to do the following things:
# 
# Change the array nums such that the first k elements of nums contain the 
# unique elements in the order they were present in nums initially. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

def removeDuplicates(self,nums):
    if not nums:
        return 0  # If the list is empty, return 0
    k = 1  # Initialize k as 1 because the first element is always unique
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:  
            nums[k] = nums[i]  # Place it in the next unique position
            k += 1  # Increment k for the next unique element
    return k  # k is the number of unique elements in the array