

def push_zero(a):
    count=0
    for i in range(len(a)):
        if a[i]!=0:
            a[count]=a[i]
            count+=1
        
    while count<len(a):
        a[count]=0
        count+=1
    
    return a
            










a=[1,2,0,2,0,8,2,0,2,3,6,4,5,2,0]
b=push_zero(a)
print(b)