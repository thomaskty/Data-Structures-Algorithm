
def sum(array):
    n=0
    final_sum = 0 
    while n<=len(array)-1:
        final_sum+=array[n]
        n+=1 
    return final_sum 

def recursive_sum(array, index=0):
    # Base case: if the index is equal to the length of the array, return 0
    if index == len(array):
        return 0
    
    # Recursive case: add the current element to the sum of the rest of the array
    return array[index] + recursive_sum(array, index + 1)



input_ar = [4,2,1,4,2]
print(recursive_sum(input_ar))




    

    