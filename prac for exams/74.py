


def isprime(n):
    if n<2:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    




def generate(a):
    primes=[]
    for i in range(2,a):
        if isprime(i):
            primes.append(i)
    return primes


a=int(input("Enter the numbers"))
primes=generate(a)
print(primes)