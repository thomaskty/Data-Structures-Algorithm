def minimum(ar):
    min_value = ar[0]
    max_value = ar[0]
    for i in range(0,len(ar)):
        if min_value>=ar[i]:
            min_value = ar[i]
        if max_value<=ar[i]:
            max_value = ar[i]
    return {'minimum':min_value,'maximum':max_value}


minimum([913,482,478,27,81,39])

