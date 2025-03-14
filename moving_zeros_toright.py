
def move_zeros_using_extra_memory(ar):
    output_array = []
    zero_count = 0 
    for i in ar:
        if i!=0:
            output_array.append(i)
        else:
            zero_count+=1 
    output_array +=[0 for i in range(zero_count)]
    print(output_array)


def move_zeros(ar):
    start,end = 0,0
    
    # we majorly move the end index:
    # move the start index only if we meet a nonzero value
    
    while end <len(ar):
        # if the value is non zero we will swap with the start section 
        if ar[end] !=0:
            ar[start],ar[end] = ar[end],ar[start]
            start +=1
            end +=1
        # if the value is zero, 
        elif ar[end]==0:
            end+=1
        print(ar)

array = [0,1,9,6,45,0,3,0]
move_zeros(array)

