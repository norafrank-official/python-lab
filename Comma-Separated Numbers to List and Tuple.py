user_input = input("Enter comma-separated numbers: ")

list_data = user_input.split(",")
tuple_data = tuple(list_data)

print(f"List: {list_data}")
print(f"Tuple: {tuple_data}")
print(f"Total number of elements: {len(list_data)}")
print(f"First element: {list_data[0]}")
print(f"Last element: {list_data[-1]}")
print(f"List in reverse order: {list_data[::-1]}")
