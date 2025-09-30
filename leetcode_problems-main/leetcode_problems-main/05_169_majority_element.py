# Given an array nums of size n, return the majority element.
# 
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.
# 
#  
# 
# Example 1:
# 
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# 
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#  
# 
# Constraints:
# 
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
# 

class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num  # New candidate
                count = 1

            elif num == candidate:
                count += 1  # Same candidate, increment count
            else:
                count -= 1  # Different element, decrement count
  
        print(candidate)
    
    # using extra memory and hash map 
    def mode_count(self,array):
        h = {}
        mode_value,mode  =0,0 
        for num in array:
            if num in h:
                h[num]+=1
                if h[num]>mode:
                    mode_value,mode = num,h[num] 
            else:
                h[num] = 1
        print(h,mode_value,mode)

solution = Solution()

array = [1,3,2,1,2,2,1,1,3]

solution.majorityElement(array)
solution.mode_count(array)
