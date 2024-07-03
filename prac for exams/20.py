str='hlloh'
def check(a):
    fg=True
    b=len(a)//2
    for c in range(b):
        if (a[c]!=a[-c-1]):
            fg=False
            break
        else:
            fg=True
    return fg


print(check(str))
