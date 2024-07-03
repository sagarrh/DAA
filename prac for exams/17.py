def swap(a):
    if len(a)<2:
        return 
    else:
        return a[-1]+a[1:-1]+a[0]

b="jonsnow"
print(swap(b))