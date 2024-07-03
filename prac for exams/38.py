

def can_make_same(a):
    count1=a.count("0")
    count0=a.count("1")
    if count1==len(a)-1 or count0==len(a)-1:
        return "yes"
    else:
        return "false"







a=input("Enter a bianry string")
print(can_make_same(a))