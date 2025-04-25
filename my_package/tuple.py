my_tuple = (1, 2, 3)

# Convert to list
temp_list = list(my_tuple)

# Append using  for 
for i in range(4, 7):
    temp_list.append(i)

# Converting to tuple 
my_tuple = tuple(temp_list)
print(my_tuple)

#using extend l,l
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

#using extend l,t
list1 = [10, 20]
tuple1 = (30, 40)
list1.extend(tuple1)
print(list1)

list1 = ['a', 'b']
list1.extend("cd")
print(list1)

