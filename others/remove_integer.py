def removeElement(nums, val):
    k = 0  # Pointer for the new length of the array with elements that are not equal to val
    
    # Iterate through the array using the pointer i
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  # Move the valid element to the "front" of the array
            k += 1  # Increment k to keep track of the next valid position
    
    return k  # The new length of the array where all elements are not equal to val


