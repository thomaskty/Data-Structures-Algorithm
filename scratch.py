
# values = 0,1,1,2,3,5,8,13,...
# index  = 0,1,2,3,...
def fibanacci_series(index):
    if index ==0:
        return 0 
    elif index ==1:
        return 1 
    else:
        return fibanacci_series(index-1)+fibanacci_series(index-2)

# for i in range(10):
#    print(i,fibanacci_series(i))

## factorial
def factorial(index):
    if index<=1:
        return 1 
    else:
        return factorial(index-1)*index
    
# for i in range(10):
#     print(i,factorial(i))

def prime(number):
    pass 


