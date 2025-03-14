# using boyer moores algorithm 
def majorityElement(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num  # New candidate
            count = 1
            
        elif num == candidate:
            count += 1  # Same candidate, increment count
        else:
            count -= 1  # Different element, decrement count
        print(num,candidate,count)
    return candidate


array = [1,3,3,2,1,2,3,3,2,1,1,3]
majorityElement(array)

# using extra memory and hash map 
def mode_count(array):
    h = {}
    mode_value,mode  =0,0 
    for num in array:
        if num in h:
            h[num]+=1
            if h[num]>mode:
                mode_value,mode = num,h[num] 
        else:
            h[num] = 1
    return h,mode_value,mode


mode_count(array)


