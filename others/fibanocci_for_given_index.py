
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
    

def fib_iterative(n):
    if n == 0 or n == 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fib_memoization(n, memo={0: 1, 1: 1}):
    if n in memo:
        return memo[n]
    memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]

def fib_recursive(n):
    if n == 0 or n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


