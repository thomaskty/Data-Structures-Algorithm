

"""
1_88. Merge sort array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order.The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].

Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
""" 

def merge(nums1, m, nums2, n):
    mp, np = m - 1, n - 1  
    
    # Start from the last valid elements in both arrays
    # Iterate backward through nums1 to fill it with sorted elements
    
    for main_pointer in range(len(nums1) - 1, -1, -1):
        # If nums2 is exhausted (np < 0), just copy remaining nums1 elements
        if np < 0:
            break
        if mp >= 0 and nums1[mp] > nums2[np]:  # Compare elements from nums1 and nums2
            nums1[main_pointer] = nums1[mp]
            mp -= 1
        else:
            nums1[main_pointer] = nums2[np]
            np -= 1
        # print(nums1)  
        # Print after each placement (can be removed if you don't need   debugging)
    return nums1 

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1,m,nums2,n)




"""
2_27. Remove element
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val. Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things. Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums. Return k.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,,]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,,,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.

Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""
def removeElement(nums, val):
    k = 0  # Pointer for the new length of the array with elements that are not equal to val

    # Iterate through the array using the pointer i
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  # Move the valid element to the "front" of the array
            k += 1  # Increment k to keep track of the next valid position
    
    return k  # The new length of the array where all elements are not equal to val


"""
3_26. Remove duplicates from sorted array
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums. Return k.

Example 1:

Input: nums = [1,1,2] Output: 2, nums = [1,2,_] Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively. It does not matter what you leave beyond the returned k (hence they are underscores). Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4] Output: 5, nums = [0,1,2,3,4,,,,,_] Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:

1 <= nums.length <= 3 * 104 -100 <= nums[i] <= 100 nums is sorted in non-decreasing order.
"""

def removeDuplicates(nums):
    if not nums:
        return 0  # If the list is empty, return 0
    k = 1  # Initialize k as 1 because the first element is always unique
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:  
            nums[k] = nums[i]  # Place it in the next unique position
            k += 1  # Increment k for the next unique element
    return k  # k is the number of unique elements in the array


"""
4_80. Remove duplicates from sorted array II
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: nums = [1,1,1,2,2,3] Output: 5, nums = [1,1,2,2,3,_] Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively. It does not matter what you leave beyond the returned k (hence they are underscores). Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3] Output: 7, nums = [0,0,1,1,2,3,3,,] Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:

1 <= nums.length <= 3 * 104 -104 <= nums[i] <= 104 nums is sorted in non-decreasing order.
"""
def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    j = 2  # Pointer for valid elements (since first two elements are always valid)

    for i in range(2, len(nums)):
        if nums[i] != nums[j - 2]:  # Check if current number can be included
            nums[j] = nums[i]
            j += 1

    return j  # Length of the modified array

"""
5_169 Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3] Output: 3 Example 2:

Input: nums = [2,2,1,1,1,2,2] Output: 2

Constraints:

n == nums.length 1 <= n <= 5 * 104 -109 <= nums[i] <= 109
"""

def majorityElement(nums):
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
    return candidate


"""
6_189. Rotate Array
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative. Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3 Output: [5,6,7,1,2,3,4] Explanation: rotate 1 steps to the right: [7,1,2,3,4,5,6] rotate 2 steps to the right: [6,7,1,2,3,4,5] rotate 3 steps to the right: [5,6,7,1,2,3,4] Example 2:

Input: nums = [-1,-100,3,99], k = 2 Output: [3,99,-1,-100] Explanation: rotate 1 steps to the right: [99,-1,-100,3] rotate 2 steps to the right: [3,99,-1,-100]

Constraints:

1 <= nums.length <= 105 -231 <= nums[i] <= 231 - 1 0 <= k <= 105

Follow up:

Try to come up with as many solut
"""

def rotate(nums,k):
    ar = nums 
    k = k%len(ar) 
    i,j = 0,len(ar)-1 
    while i<j:
        ar[i],ar[j] = ar[j],ar[i]
        i+=1
        j-=1
        
    i,j = 0,k-1
    while i<j:
        ar[i],ar[j] = ar[j],ar[i]
        i+=1
        j-=1
        
    i,j = k,len(ar)-1 
    while i<j:
        ar[i],ar[j] = ar[j],ar[i]
        i+=1
        j-=1
        
        
"""
8_121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4] Output: 5 Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5. Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell. Example 2:

Input: prices = [7,6,4,3,1] Output: 0 Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

1 <= prices.length <= 105 0 <= prices[i] <= 104 
"""

def maxProfit(nums):
    buy = nums[0]
    maxprofit = 0
    for i in range(0,len(nums)):
        if nums[i]<buy:
            buy = nums[i]

        profit = nums[i]-buy
        if profit>maxprofit:
            maxprofit = profit

    return maxprofit


"""
9_122. Best Time to Buy and Sell Stock II
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4] Output: 7 Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3. Total profit is 4 + 3 = 7. Example 2:

Input: prices = [1,2,3,4,5] Output: 4 Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4. Total profit is 4. Example 3:

Input: prices = [7,6,4,3,1] Output: 0 Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

Constraints:

1 <= prices.length <= 3 * 104 0 <= prices[i] <= 104
"""
def maxProfit(prices):
    total_profit = 0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            total_profit += prices[i]-prices[i-1]
    return total_profit

"""
10_55 Jump Game I
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1: Input: nums = [2,3,1,1,4] Output: true Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2: Input: nums = [3,2,1,0,4] Output: false Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

Constraints:

1 <= nums.length <= 104 0 <= nums[i] <= 105
"""
def canJump(nums):
    goal = len(nums)-1
    for i in range(len(nums)-2,-1,-1):
        print(goal,i)
        if i+nums[i]>=goal:
            goal=i
    print(goal,i)
    if goal==0:
        return True
    else:
        return False
    
"""
11_45 Jump Game II
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0]. Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and i + j < n Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:

Input: nums = [2,3,1,1,4] Output: 2 Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index. Example 2:

Input: nums = [2,3,0,1,4] Output: 2

Constraints:

1 <= nums.length <= 104 0 <= nums[i] <= 1000 It's guaranteed that you can reach nums[n - 1]
"""
def jump(nums):
    res = 0 
    l = r = 0 
    while r<len(nums)-1:
        farthest = 0
        for i in range(l,r+1):
            farthest = max(farthest,i+nums[i])
        l = r+1 
        r = farthest
        res +=1
    return res

