#To generate different patterns of stars.

# To generate the star square pattern.
n=int(input("Enter the value of number:"))
for i in range (n): # i will creat the row
    for j in range(n):# j will creat the column
        print("*",end=" ")
    print()

# To generate the Right-Angled Triangle.
n=int(input("Enter the value of number:"))
for i in range (n+1): # i will creat the row
    for j in range(i):# j will creat the column
        print("*",end=" ")
    print() 

# To generate the inverted-right angle triangle.
n=int(input("Enter the value of number:"))
i=n
while i>=1: # i will creat the row
    for j in range(i):# j will creat the column
        print("*",end=" ")
    print()
    i-=1 

# Incresing Number Pattern.
n=int(input("Enter the number:"))
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
    num=num+1
    print()

# Pyramid Star Pattern.
n=int(input("Enter the number:"))
for i in range (1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        print("*",end=" ")
    print()   