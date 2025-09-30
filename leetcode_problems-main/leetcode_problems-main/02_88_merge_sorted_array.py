
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# 
# Example 1:
# 
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:
# 
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:
# 
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
#  
# 
# Constraints:
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109
#  
# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

class Solution:
    def merge1(self, nums1 , m, nums2, n) -> None:
        """
        space complexitty : 0(1) 
        time complexity : o(m+n)
        Do not return anything, modify nums1 in-place instead.
        """
        mp, np = m - 1, n - 1  # Start from the last valid elements in both arrays
        # Iterate backward through nums1 to fill it with sorted elements
        for main_pointer in range(len(nums1) - 1, -1, -1):
            # If nums2 is exhausted (np < 0), just copy remaining nums1 elements
            # if nums2 is over then dont do anything keep the 
            if np < 0:
                break

            if mp >= 0 and nums1[mp] > nums2[np]:  # Compare elements from nums1 and nums2
                nums1[main_pointer] = nums1[mp]
                mp -= 1
            else:
                nums1[main_pointer] = nums2[np]
                np -= 1

            # print(nums1)  # Print after each placement (can be removed if you don't need   debugging)
        return nums1 

    def merge2(nums1:list[int], m:int, nums2:list[int], n:int) -> None:
        '''
        space complexitty : 0(1) 
        time complexity : o(m+n)
        approach : create additional index for filling the positions.
        compare the last values of both arrays 
        '''
        # Initialize pointers for nums1 and nums2
        i, j, k = m - 1, n - 1, m + n - 1
    
        # Merge nums1 and nums2 in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
    
        # If there are remaining elements in nums2, copy them to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

solution = Solution()

# Example usage:
nums1= [3,9,12,24,0,0,0,0]
nums2 = [5,10,11,36]
m = 4
n = 4

solution.merge1(nums1, m, nums2, n)
print(nums1)

