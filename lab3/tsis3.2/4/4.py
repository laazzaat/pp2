def isPrime(x):
    if(x == 1):
        return False
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True

def filtr(numbers):
    return list(filter(isPrime, numbers))

listik = [1,2,3,4,5,6,7,8,9,10,11]
primes = filtr(listik)

print("Prime numbers in the list:", primes)