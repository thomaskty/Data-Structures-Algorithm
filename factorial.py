

def factorial(n):
    if n<=1:
        return 1
    else:
        return factorial(n-1)*n

for i in range(10):
    print(factorial(i),end=',')
    