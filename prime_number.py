
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

