a =int(input("sv "))

def check(a):
    count=0
    while a>10:
        a=a//6
        count+=1
    return count



print(check(a))