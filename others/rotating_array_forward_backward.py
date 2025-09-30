

# rotating an array forward by one step 
def rotate_forward(ar):
    for i in range(len(ar)-1):
        ar[0],ar[i+1] = ar[i+1],ar[0]
    return ar

# rotating an array backward by one step 
def rotate_backwards(ar):
    j = len(ar)-1
    i = len(ar)-2
    while i>=0:
        ar[i],ar[j] = ar[j],ar[i]
        i -=1
    return ar

# testing 
input_ar = [3812,2,8,22,3,1,2,49,73]
output  = rotate_forward(input_ar)
print(output)

