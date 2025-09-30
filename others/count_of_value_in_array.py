
# finding count of value in a sorted array 
def find_count(ar,value):
    first = find_first_occurence(ar,value)
    last = find_first_occurence(ar,value,first =False)
    if first==-1:
        return -1
    else:
        count = (last -first)+1 
        return count

