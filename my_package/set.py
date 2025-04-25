#set 
my_set = {1, 2, 3, 4}
another_set = set([3, 4, 5, 6])
for item in my_set:
    print(item)

#set operations
A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))            
print(A.intersection(B))    
print(A.difference(B))         
print(A.symmetric_difference(B))

