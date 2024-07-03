def pytho_limit(some):
    triplet=[]
    for a in range(1,some+1):
        for b in range(1,some+1):
            c=((a**2)+(b**2))**0.5
            if c==int(c) and c<=some:
                triplet.append((a,b,int(c)))


    return triplet






num=int(input("enter a number"))
triplet=pytho_limit(num)
for each in triplet:
    print(each)