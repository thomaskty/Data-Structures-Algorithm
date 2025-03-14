# finding the second largest number in an array 
def second_max(arr_):
    max_ = max(arr_) 
    arr_.remove(max_) 
    second_max = max(arr_)
    return second_max 
