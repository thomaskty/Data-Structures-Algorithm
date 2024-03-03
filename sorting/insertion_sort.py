
def insertionSort(arr):
    n = len(arr) # Get the length of the array
    if n <= 1:
        return # If the array has 0 or 1 element, it is already sorted, so return

    for i in range(1, n): # Iterate over the array starting from the second element
        key = arr[i] # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]: # Move elements greater than key one position ahead
            arr[j+1] = arr[j] # Shift elements to the right
            j -= 1
        arr[j+1] = key # Insert the key in the correct position

    return arr 

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        # looping over the sorted part reverse manner( to put the key ) 
        for j in range(i-1,-1,-1):
            last_changed_index = 'NA'
            if arr[j]>key:
                last_changed_index = j
                arr[j+1] = arr[j]
            if last_changed_index != 'NA':
                arr[last_changed_index] = key
    return arr

def insertion_sort_2(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        # looping over the sorted part reverse manner( to put the key ) 
        for j in range(i-1,-1,-1):
            if arr[j]>key:
                arr[j+1] = arr[j]
                arr[j] = key
    return arr 

def insertion_sort_3(ar):
    for i in range(1,len(ar)):
        j = i-1
        key = ar[i] 
        while j>=0:
            if key<ar[j]:
                ar[j+1] = ar[j]
                ar[j] = key 
            j-=1
    return ar 


test_cases = [
    [38,2,1,98,99,8766,887,432,4],
    [1,32,12,35,388,92,43,4,2,2,3,2,2,5,0,24,9]
]
for case in test_cases:
    print(insertion_sort_2(case))



