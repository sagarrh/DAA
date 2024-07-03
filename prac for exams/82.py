import numpy as np

a=np.array([2,4,1,8,10,9])
b=np.array([4,11,8,14,3])

newlist=[]
for each in a:
    if each not in b:
        newlist.append(each)

print(sorted(newlist))