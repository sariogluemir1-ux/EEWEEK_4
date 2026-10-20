s = "abcabc"
unique_chars = ""
for char in s:
    if char not in unique_chars:
        unique_chars += char
unique_count = len(unique_chars)
print(f"The number of unique letters in '{s}' is: {unique_count}")
