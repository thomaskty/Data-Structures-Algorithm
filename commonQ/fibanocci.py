
# recursive implementation of fibanocci series 
def fibanocci_recursion(n):
    if n==0:
        return 0 
    elif n==1:
        return 1 
    else:
        return fibanocci_recursion(n-1)+fibanocci_recursion(n-2)
    
# testing the series 
print('recursive implementation --- ')
for j in range(10):
    print(fibanocci_recursion(j),end = ' ')


# while loop implementation of fibanocci series 
print('\nwhile loop implementation ---')
def fibanocci_while(n):
    if n==0:
        return 0 
    elif n==1:
        return 1 
    else:
        a,b = 0,1
        i = 0
        while i< n-1:
            next_value = a+b 
            a,b = b,next_value
            i+=1 
        return b

for j in range(10):
    print(fibanocci_while(j),end = ' ')
    