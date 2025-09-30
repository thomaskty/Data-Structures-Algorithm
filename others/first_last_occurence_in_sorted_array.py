
# first and last occurence of a sorted array 
def find_first_occurence(ar,value,first =True):
    start,end = 0,len(ar)-1
    result = -1 
    while start<=end:
        mid = int((start+end)/2)
        if value == ar[mid]:
            if first == True:
                end = mid -1
            else:
                start = mid+1 
            result = mid 
        elif value <ar[mid]:
            end = mid -1 
        elif value >ar[mid]:
            start = mid+1 
    return result
