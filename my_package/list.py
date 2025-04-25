#1.creation list
list = [10,20,30,40,50]
print("list",list)
list1 =["java","python","c"]
print("list1:",list1)
list2 = [10,"python",45.34,'p']
print("list2:",list2)

#2.usage of range fn
list1 = range(10)
for i in list1:
    print(i,end=' ')
print("\n")
list2 = range(5,10)
for j in list2:
    print(j,end=' ')

x=[]
print('How many elements?',end='')
n = int(input())
#accept the element values and populate in the list
for i in range(n):
   print('Enter the element',end=' ')
   x.append(int(input()))
   print('The elements of the list are',x)

#find the smallest and largest element of the list
big=x[0]
small=x[0]

for i in range(1,n):
   if x[i]>big: big=x[i]
   if x[i]<small: small=x[i]
print('Smallest element is',small)
print('Largest element is',big)

#element to count
x=[]
n = int(input("How many elements?"))

for i in range(n):
   print('enter the element',end='')
   x.append(int(input()))
print('the elements are',x)

y = int(input("Enter the elements to count"))
c=0
for i in x:
   if(y==i): c+=1
print('{} is found {} times'.format(y,c))

#nested list
mat = [[1,2,3],[4,5,6],[7,8,9]]
print('Display the list elements are')
print(mat)
print('Display row by row')
for r in mat:
   print(r)
print('Display each column in row1')
for c in mat[0]:
   print('%d' %c,end=' ')
print("\n")

#List Data Structure
my_list = [10, 20, "Sai", 3.14, True]
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  
print(fruits[-1]) 
fruits[1] = "orange"
print(fruits)  
fruits.append("grape")         
fruits.insert(1, "kiwi")       

fruits.remove("apple")          
fruits.pop()                   
fruits.pop(0)    
print(fruits[1:3])  
for fruit in fruits:
    print(fruit)
print(len(fruits))

#5.list append
list1 = [1, 2, 3]
list2 = [4, 5, 6]
for item in list2:
    list1.append(item)
print(list1) 



