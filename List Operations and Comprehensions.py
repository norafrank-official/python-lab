numbers = [10, 25, 42, 19, 33, 50, 7, 88]
print(f"Original List: {numbers}")

filtered_numbers = [x for x in numbers if x > 30]
print(f"Filtered (Numbers > 30): {filtered_numbers}")

search_val = int(input("Enter a number to search: "))
if search_val in numbers:
    print(f"{search_val} found at index {numbers.index(search_val)}")
else:
    print(f"{search_val} not found in the list.")

index_to_update = int(input("Enter index to update (0 to 7): "))
new_value = int(input("Enter new value: "))
numbers[index_to_update] = new_value
print(f"Updated List: {numbers}")

numbers.append(99)
numbers.sort(reverse=True)
print(f"Manipulated List (Sorted descending with added element): {numbers}")
