# Original string
text = "   Hello, Python!   "

# 1. strip()
clean_text = text.strip()
print(f"Stripped: '{clean_text}'")

# 2. max() and min()
max_char = max(text)
min_char = min(text)
print(f"Max character: {max_char}")
print(f"Min character: {min_char}")

# 3. upper() and lower()
uppercase_text = text.upper()
lowercase_text = text.lower()
print(f"Uppercase: {uppercase_text}")
print(f"Lowercase: {lowercase_text}")

# 4. replace()
replaced_text = text.replace("Python", "World")
print(f"Replaced text: {replaced_text}")

# 5. find()
index = text.find("Python")
not_found_index = text.find("Java")
print(f"Index of 'Python': {index}")
print(f"Index of 'Java': {not_found_index}")

# 6. split()
split_text = text.split(", ")
print(f"Split text: {split_text}")
