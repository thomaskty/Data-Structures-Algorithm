
def merge(left,right):
    total_len = len(left)+len(right)
    final_array = list(range(total_len))
    i = 0 
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] <=right[j]:
            final_array[k] = left[i]
            i+=1
        else:
            final_array[k] = right[j]
            j+=1
        k+=1
        print(final_array)

    while i<len(left):
        final_array[k] = left[i]
        i+=1
        k+=1
        print(final_array)

    while j<len(right):
        final_array[k] = right[j]
        j+=1 
        k+=1 
        print(final_array)
        
    
left = [4,5,9]
right = [8,9,12,20]
merge(left,right)
