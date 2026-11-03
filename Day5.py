# Swapping of two numbers.
# Using Third veriable
a=int(input("Enter the value of first number:"))
b=int(input("Enter the value of second number:"))
print("Befor swapping of two numbers:","a=",a,"b=",b)
c=a
a=b
b=c
print("After swapping of numbers:","a=",a,"b=",b)

# Without using Third veriable.
a=int(input("Enter the value for a:"))
b=int(input("Enter the value for b:"))
print("befor swapping of two numbers:","a=",a,"b=",b)
a=a+b
b=a-b
a=a-b
print("After swapping of two numbers:","a=",a,"b=",b)