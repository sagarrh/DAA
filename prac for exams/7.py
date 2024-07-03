my_dict = {'a': 1, 'b': 2, 'c': 3}

ktr='b'
if ktr in my_dict:
    del my_dict[ktr]
    print("sucess")
else:
    print("fail")

print("Updated Dictionary:", my_dict)