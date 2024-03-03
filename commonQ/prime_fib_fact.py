
# whether the input number is prime or not 
# definition of prime : a whole number greater than 1 that 
# cannot be exactly divided by any whole number other than itself and 1

def prime(value):
    prime = True
    check_list = list(range(2,value//2+1))
    print(check_list)
    for i in check_list:
        if value%i==0:
            prime = False
            break
    return prime

def isprime(n):
    prime = True
    if n>1:
        half_numbers = range(2,int(n/2)+1)
        for i in half_numbers:
            if n%i ==0:
                prime = False
                break
        return prime
    else:
        return False

print('first 100 prime numbers ... ')
for i in range(1,50):
    if isprime(i):
        print(i,end=',')
print('\n')        
 

# -> input (7,6)
# -> (7,5)
# -> (7,4)
# -> (7,3)
# -> (7,2)
# -> (7,1) => False
# -> None of the above numbers can divide the input number except 1 

# -> input (4,3)
# -> (4,2) -> False (divisible by 2) 
       
def is_prime(n, i):
    if n <= 1:
        return False
    if i == 1:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i - 1)


# Example usage:
print('printing first 100 prime numbers ... ')
for i in range(0,50):
    if is_prime(i,i-1):
        print(i,end=',')

print('\n')

# find factorial of a given number 
def factorial(n):
    output = 1
    for i in range(1,n+1):
        output*=i
    return output

print('printing factorial of numbers from 0 to 10')
for i in range(10):
    print(i,factorial(i))

# fibanocci series as output at a given n 
# if n = 0, output = 0 
# if n = 1, output = 1 
# if n = 2, output = 1
# if n = 3, output = 2
# if n = 4, output = 3

# [0,1,2,3,4] : inputs 
# [0,1,1,2,3] : output


def fibanacci(n):
    if n<=2:
        return 1
    else:
        return fibanacci(n-1)+fibanacci(n-2)
print('printing fibanacci values of indexes from 0 to 10')
for i in range(10):
    print(i,fibanacci(i))
    