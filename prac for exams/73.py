def sumofdigits(a):
    sum=0
    while a>0:
        digit=a%10
        sum=sum+digit
        a=a//10
    return sum

print(sumofdigits(16789))