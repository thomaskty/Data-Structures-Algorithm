
def min_max(ar):
    min_ = ar[0]
    max_ = ar[0]
    for i in range(len(ar)):
        if ar[i]<=min_:
            min_= ar[i] 
        if ar[i]>=max_:
            max_ = ar[i] 
    return min_,max_

output = min_max([913,482,478,27,81,39])
print(output) 
