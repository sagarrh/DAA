sample= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

unique=set()

for item in sample:
    for values in item.values():
        unique.add(values)

print("unique values",unique)
