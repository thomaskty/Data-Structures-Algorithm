
def merge(nums1,nums2,m,n):
    i,j = m-1,n-1
    for k in range(len(nums1)-1,-1,-1):
        if j<0:
            break
        if nums1[i]>nums2[j]:
            nums1[k] = nums1[i]
            i-=1
        else:
            num

# Example usage:
nums1= [3,9,12,24,0,0,0,0]
nums2 = [5,10,11,36]
m = 4
n = 4

merge(nums1,nums2, m,n)
print(nums1)

