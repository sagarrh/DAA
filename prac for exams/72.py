def printdict():
    n = int(input("enter the number"))
    dict={}
    for i in range(1,n+1):
        dict[i]=i**2

    print(dict)

printdict()