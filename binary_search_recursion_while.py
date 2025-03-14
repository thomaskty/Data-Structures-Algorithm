# binary search recursive implementation 
def binary_search(ar,value,start,end):
    if start<=end:
        middle = int((start+end)/2) # finding the middle 
        if value == ar[middle]: 
            return middle
        elif value>ar[middle]:  
            return binary_search(ar,value,middle+1,end)
        elif value<ar[middle]:
            return binary_search(ar,value,start,middle-1)
    else:
        return -1

# binary search while loop implementation  
def binary_search_while(ar,value):
    start,end = 0,len(ar)-1
    while start<=end:
        mid = int((start+end)/2)
        if value == ar[mid]:
            return mid 
        elif value>ar[mid]:
            start = mid+1 
        elif value<ar[mid]:
            end = mid-1
    else:
        return -1
