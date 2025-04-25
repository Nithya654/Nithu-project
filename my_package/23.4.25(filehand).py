#  r – Read (Text Mode)
# Opens an existing file for reading. If the file does not exist, it raises an error.

with open(r'C:\Users\nithy\OneDrive\Documents\training 19 march\march25\hello.txt', 'r') as file:
    content = file.read()
    print(content)

#rb – Read (Binary Mode)
with open(r'C:\Users\nithy\OneDrive\Documents\training 19 march\march25\hello.txt', 'rb') as file:
    data = file.read()
    print(data[:10])  # First 10 bytes

#r+ – Read and Write (Text Mode)
with open(r'C:\Users\nithy\OneDrive\Documents\training 19 march\march25\hello.txt', 'r+') as file:
    print("Before:", file.read())
    file.seek(0)
    file.write("Updated text")

#rb+ – Read and Write (Binary Mode)
with open(r"C:\Users\nithy\Downloads\hello.bin", 'rb+') as file:
    data = file.read()
    file.seek(0)
    file.write(b'12345')

#w – Write (Text Mode)
with open(r'C:\Users\nithy\OneDrive\Documents\training 19 march\march25\hello.txt', 'w') as file:
    file.write("This will overwrite the file.")
    print(content)

#wb – Write (Binary Mode)
with open(r'C:\Users\nithy\OneDrive\Documents\training 19 march\march25\hello.bin', 'wb') as file:
    file.write(b'\x00\x01\x02')

#w+ – Write and Read (Text Mode)
with open(r'C:\Users\nithy\OneDrive\Documents\training 19 march\march25\hello.txt', 'w+') as file:
    file.write("W+ mode content")
    file.seek(0)
    print(file.read())

#wb+ – Write and Read (Binary Mode)
with open(r'C:\Users\nithy\OneDrive\Documents\training 19 march\march25\hello.bin', 'wb+') as file:
    file.write(b'Binary data')
    file.seek(0)
    print(file.read())

#a – Append (Text Mode)
with open(r'C:\Users\nithy\OneDrive\Documents\training 19 march\march25\hello.txt', 'a') as file:
    file.write("\nAppended line")

#ab – Append (Binary Mode)
with open(r'C:\Users\nithy\OneDrive\Documents\training 19 march\march25\hello.bin', 'ab') as file:
    file.write(b'\x03\x04')
    print(content)

#a+ – Append and Read (Text Mode)
with open(r'C:\Users\nithy\OneDrive\Documents\training 19 march\march25\hello.txt', 'a+') as file:
    file.write("\nNew line in a+")
    file.seek(0)
    print(file.read())

#ab+ – Append and Read (Binary Mode)
with open(r'C:\Users\nithy\OneDrive\Documents\training 19 march\march25\hello.bin', 'ab+') as file:
    file.write(b'\x05\x06')
    file.seek(0)
    print(file.read())


