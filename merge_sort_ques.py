
# leet code problem 
def merge(nums1:list[int], m:int, nums2:list[int], n:int):
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

# Example usage:
nums1= [3,9,12,24,0,0,0,0]
nums2 = [5,10,11,36]
m = 4
n = 4

merge(nums1, m, nums2, n)
print(nums1)
