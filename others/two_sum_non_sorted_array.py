
# Write a Python function to find two numbers in an unsorted array that add up to a given target. 
# Implement two different approaches:
#  * Brute-force approach: Check all possible pairs (O(n²) complexity).
#  * Hashmap-based approach: Use a dictionary to achieve an O(n) time complexity solution.
# ```python
# ar = [4, 7, 1, -3, 2]
# target = 5
# print(two_sum_brute_force(ar, target))  # Output: [1, 4] (since 4 + 1 = 5)
# print(two_sum_hashmap(ar, target))      # Output: [1, 4]
# ```
# Constraints:
# * The input list is unsorted and may contain positive and negative numbers.
# * There is exactly one solution, meaning only one unique pair exists.
# * The function should return 1-based indices (not zero-based).
# * Brute-force approach should check all possible pairs (O(n²) complexity).
# * Hashmap-based approach should use a dictionary to find the solution efficiently (O(n) complexity).

def two_sum(numbers, target): # o(n) 
    h = {}    
    for i, num in enumerate(numbers):
        desired = target - num
        if desired in h: 
            # return num,desired # returning the numbers 
            return (h[desired],i) # returning the indexes of numbers 
        h[num] = i   

def bruteforce_two_sum(ar,target): # o(n2) 
    length = len(ar)
    for i in range(length-1):
        for j in range(i+1,length):
            if target==ar[i]+ar[j]:
                return (i,j) # returning the indexes; 


ar = [3,29,9,13,4,2]
output_1 = two_sum(ar,5)
output_2 = bruteforce_two_sum(ar,5)
print(output_1)
print(output_2)

