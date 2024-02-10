def isPrime(x):
    if(x == 1):
        return False
    for i in range(2, x):
        if(x % i == 0):
            return False
    return True

class List():
    def __init__(self, a):
        self.a = a
    def filtering(self):
        return list(filter(lambda x : isPrime(x), self.a))

example = List([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(example.filtering())