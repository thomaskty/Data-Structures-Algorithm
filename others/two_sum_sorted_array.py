# Question: Write a Python function to find two numbers in a sorted array that add up to a given target. 
# The function should return the indices (1-based) of the two numbers. 
# The solution should run in O(n) time complexity using the two-pointer technique.

# ar = [1, 2, 3, 4, 6, 8, 11]
# target = 10
# print(two_sum(ar, target))
# # Output: [3, 5]  (since 3 + 6 = 10)
# Constraints:
# 
# The input list is sorted in ascending order.
# There is exactly one solution, meaning only one unique pair exists.
# The function should return 1-based indices (not zero-based).
# The function should run in O(n) time complexity using two pointers.

def two_sum_sorted(ar,target):
    i,j = 0,len(ar)-1
    while i<j:
        _sum = ar[i]+ ar[j]
        if _sum <target:
            i+=1
        elif _sum>target:
            j-=1
        else:
            return i+1,j+1 

ar = [1,2,3,4,6,8,11]
output_final = two_sum_sorted(ar,target=10)
output_final2 = bruteforce_two_sum(ar,target=10)
print(output_final)
print(output_final2)

