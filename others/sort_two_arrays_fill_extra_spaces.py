
'''
given two arrays ar1, ar2 : ar1 has sufficient extra
space with 0s in order to be filled and sorted.
'''

def merge_sorted(ar1,ar2):

    j = len(ar2) -1
    i = len(ar1)- len(ar2) -1
    k = (i+j) -1

    while i>=0 and j>=0:
        if ar2[j]>ar1[i]:
            print(ar1)
            ar1[k] = ar2[j]
            ar2.remove(ar2[j])

            j = j-1
            k = k-1
        else:
            print(ar1)
            ar1[k] = ar1[i]
            i = i -1
            k = k-1

    if i == 0:
        ar1[:j] = ar2
    if j == 0:
        ar1[:i] = ar1

    return ar1



def merge_sorted_arrays(nums1,nums2,m,n):
    mp, np = m - 1, n - 1  # Start from the last valid elements in both arrays
    
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
    
        print(nums1)  # Print after each placement (can be removed if you don't need debugging)
    return nums1 


nums1 = [3,5,10,0,0,0,0]
nums2 = [2,5,6,9]
m = 3
n = 4

merge_sorted_arrays(nums1,nums2,m,n)

def merge_sorted_arrays(nums1, nums2, m, n):
    mp, np = m - 1, n - 1  # Start from the last valid elements in both arrays
    main_pointer = len(nums1) - 1  # Start from the last index of nums1

    while main_pointer >= 0:
        # If nums2 is exhausted (np < 0), just copy remaining nums1 elements
        if np < 0:
            break
        
        # If there are still elements in both arrays, compare them
        if mp >= 0 and nums1[mp] > nums2[np]:
            nums1[main_pointer] = nums1[mp]
            mp -= 1
        else:
            nums1[main_pointer] = nums2[np]
            np -= 1
        
        # Move the main_pointer backwards
        main_pointer -= 1
        # Print after each placement (can be removed if you don't need debugging)

        print(nums1)  
    
    return nums1



nums1 = [3,5,10,0,0,0,0]
nums2 = [2,5,6,9]
m = 3
n = 4

merge_sorted_arrays(nums1,nums2,m,n)



