
def merge(left,right):
    total_len = len(left)+len(right)
    final_array = list(range(total_len))
    i = 0 ;j = 0 ; k = 0
    while i < len(left) and j < len(right):
        if left[i] <=right[j]:
            final_array[k] = left[i]
            i+=1
        else:
            final_array[k] = right[j]
            j+=1
        k+=1
    while i<len(left):
        final_array[k] = left[i]
        i+=1;k+=1
    while j<len(right):
        final_array[k] = right[j]
        j+=1 ; k+=1 
    return final_array 

def merge_sort_while(ar):
    middle = len(ar)//2

    left = ar[:middle]
    right = ar[middle:]
    print(left)
    print(right)

    return merge(left,right)

array = [54,26,93,17,77,31,44,55,20]

output = merge_sort_while(array)

print(output)

