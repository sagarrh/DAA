my_dict = {'a': 1, 'b': 2, 'c': 3}

def check_dictionary_function(key,dict):
    if key in dict:
        return True
    else :
        return False
    
ktc='a'
print(f"key '{ktc}' exists in the dictionary",check_dictionary_function(ktc,my_dict))

ktc='i'
print(f"key '{ktc}' exists in the dictionary",check_dictionary_function(ktc,my_dict))