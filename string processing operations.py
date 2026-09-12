text = input("Enter a string: ")

replaced_text = text.replace(" ", "-")
print(f"Replaced text: {replaced_text}")

reversed_text = text[::-1]
print(f"Reversed string: {reversed_text}")

cleaned_text = text.replace(" ", "").lower()
if cleaned_text == cleaned_text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

char_freq = {char: text.count(char) for char in set(text)}
word_freq = {word: text.split().count(word) for word in set(text.split())}
print(f"Character frequencies: {char_freq}")
print(f"Word frequencies: {word_freq}")
