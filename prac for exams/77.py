class twosum:
    def __init__(self,num):
        self.num=num
    def target(self,target):
        for i in range(1,num+1):
            for j in num:
                if num[i]+num[j]==target:
                    return i,j

num = [2, 7, 11, 15]
target = 9

a=twosum(num)
b,c=a.target(target)

