# input : [0,1,9,6,45,0,3,0]
# output : [1,3,12,0,0] ; maintain the order 

def move_zeros(ar):
    i = 0 
    j = 0 
    while i<=len(ar):
        if ar[i] !=0:
            j = i
            i+=1

        elif ar[i] ==0:
            ar[i],ar[j] = ar[j],ar[i]
            i+=1

        print(ar)

    

ar = [0,1,0,0,87,89,9,0,0,7,6,45,0,3,0]
move_zeros(ar)