def patter(rows):
    for i in range(1,rows+1):
        for j in range(i):
            print(i,end='')
        print()
        
rows = 6
patter(rows)
