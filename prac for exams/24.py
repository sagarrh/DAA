digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
vowels = ['a', 'e', 'i', 'o', 'u']


def getint(a):
    dc=0
    ssc=0
    vc=0
    cc=0
    for char in a:
        if char in digits:
            dc+=1
        elif char in special_symbols:
            ssc+=1
        elif char in vowels:
            vc+=1
        else:
            cc+=1
    return (f"count is is '{dc}', '{ssc}' ,'{vc}', '{cc}'")


setence ="625874857 rgjrh vb487hucwbet8yhw@#$%^&*g0 84t4hgj4b"
print(getint(setence))