import os

def create_file(name):
    with open(name, 'w') as f:
        f.write("Hello Hexaware!\n")

def read_file(name):
    with open(name, 'r') as f:
        print(f.read())

def append_file(name, text):
    with open(name, 'a') as f:
        f.write(text)

def rename_file(old, new):
    os.rename(old, new)

def delete_file(name):
    os.remove(name)

# Flow
filename = "file_ops.txt"
newname = "new_file_ops.txt"

create_file(filename)
append_file(filename, "This is appended.\n")
read_file(filename)
rename_file(filename, newname)
read_file(newname)
delete_file(newname)


