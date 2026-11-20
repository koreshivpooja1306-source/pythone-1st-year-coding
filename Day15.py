# To Develop Small Calculator Using Function

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        Print("Error!,Y value is Zero.")
    else:
        return x/y

a=int(input("Enter the First number:"))
b=int(input("Enter the Second number:"))
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter the choice:"))
if choice==1:
    print("Result:",add(a,b))
elif choice==2:
    subtract(a,b)
elif choice==3:
    multiply(a,b)
elif choice==4:
    divide(a,b)
else:
    print("Enter the valid choice.")


