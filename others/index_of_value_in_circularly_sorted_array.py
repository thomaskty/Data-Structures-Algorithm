

# finding index of a value in a circularly sorted array with no duplicates
def circular_search(ar,n,x):
        low = 0; high = n-1
        while low<=high:
            mid = int((low+high)/2)
            if(x==ar[mid]):  # case 1 : found x 
                return mid 
            if (ar[mid]<=ar[high]): # case 2 ; right half is sorted 
                if (x>ar[mid] and x<=ar[high]):
                    low = mid +1 
                else:
                    high = mid -1
            else:
                if (x>=ar[low] and x<ar[mid]):
                    high = mid -1 
                else:
                    low = mid+1
        return -1
