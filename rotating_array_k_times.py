def reverse(ar,k):
    i,j = 0,len(ar)-1 
    while i<j:
        ar[i],ar[j] = ar[j],ar[i]
        i+=1;j-=1
        
    i,j = 0,k-1 
    while i<j:
        ar[i],ar[j] = ar[j],ar[i]
        i+=1;j-=1
        
    i,j = k,len(ar)-1 
    while i<j:
        ar[i],ar[j] = ar[j],ar[i]
        i+=1;j-=1

array = [2,3,4,2,1,84,94,85]
reverse(array,len(array))

