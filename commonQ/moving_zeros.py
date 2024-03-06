# input : [0,1,9,6,45,0,3,0]
# output : [1,3,12,0,0] ; maintain the order 

def move_zeros(ar):
    zero_count = ar.count(0)
    array_length = len(ar)
    i = 0
    c=0
    while i<=array_length-zero_count:
        print(i,ar)
        if ((ar[i] ==0) & (ar[i+1] !=0)):
            ar[i],ar[i+1] = ar[i+1],ar[i]
            i+=1
            c+=1

        elif ((ar[i] ==0) & (ar[i+1] ==0)):
            ar[i],ar[i+2] = ar[i+2],ar[i]
            i+=1
        else:
            i+=1
        
    

    

ar = [0,1,0,0,87,89,9,0,0,7,6,45,0,3,0]
move_zeros(ar)




