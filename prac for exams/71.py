




def remove_duplicates_with_order(input_list):
    seen = set()
    result=[]
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
        
    return result










input_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
output_list = remove_duplicates_with_order(input_list)
print("Input:", input_list)
print("Output:", output_list)