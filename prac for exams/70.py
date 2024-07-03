import math

def calc(d):
    returnthis = []
    for value in d:
        prod1=2*50
        prod2=prod1/30
        prod3=prod2*value
        result=math.sqrt(prod3)

        returnthis.append(int(result))
    
    return returnthis

ls=[100,150,180]
print(calc(ls))
