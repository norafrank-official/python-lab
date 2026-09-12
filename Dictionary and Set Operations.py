set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Common elements (Intersection): {set1 & set2}")
print(f"Unique elements (Symmetric Difference): {set1 ^ set2}")

dict1 = {'a': 3, 'b': 1, 'c': 2}
dict2 = {'d': 4, 'e': 5}

sorted_dict = dict(sorted(dict1.items(), key=lambda item: item[1]))
print(f"Sorted dictionary by value: {sorted_dict}")

merged_dict = {**dict1, **dict2}
print(f"Merged dictionary: {merged_dict}")
