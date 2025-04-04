# reversing an array using pointers 
def reverse(ar):
    i = 0 
    j = len(ar)-1
    while i<=len(ar)//2:
        ar[i],ar[j] = ar[j],ar[i]
        i+=1
        j+=1
    return ar 

# reversing an array based on recursion 
def reverse_recur(ar):
    if len(ar)<=1:
        return ar 
    else:
        return reverse_recur(ar[1:])+reverse_recur(ar[:1])
