num=12345

def reverse(a):
    b=a
    newnum=0
    while a>0:
        q=a%10
        newnum=newnum*10+q
        a//=10
    return newnum

print(reverse(num))
