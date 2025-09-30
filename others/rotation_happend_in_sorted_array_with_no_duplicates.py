# rotations happend in a sorted array with no duplicates 
def get_rotations(ar,n):
    low,high = 0,n-1
    while low<=high:
        if ar[low]<=ar[high]:  # case 1 
            return low
        else:
            mid = int((low+high)/2)
            next_ = (mid+1)%n 
            prev = (mid+n-1)%n 
        if ar[mid]<=ar[next_] and ar[mid]<=ar[prev]: # case 2 
            return mid
        elif ar[mid]<=ar[high]:
            high = mid-1
        elif ar[mid] >=ar[low]:
            low = mid+1
    return -1


