
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# merged_dict = dict1 | dict2
# print(merged_dict)
# print(id(dict1))
# print(id(dict2))
# print(id(merged_dict))

print(f'{id(dict1)} - id dict1 before merge')
print(f'{dict1} - dict1 before merge')
dict1 |= dict2
print(dict1)
print(dict2)
print(id(dict1))
print(id(dict2))