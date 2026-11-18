# To manage the student information using list,tuple,dictionary,set
# Perform operation on it such as
#1.insertion,2.deletion,3.updating,4.searching

while True:
    print("1.List operations:")
    print("2.Tuple operations:")
    print("3.Dictionary operations:")
    print("4.set operations:")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
# 1.List operations
    if choice==1:
        marks=[85,90,50,40,50]
        print("\n Original Marks:",marks)
        print("1.Add Marks:")
        print("2.Remove Marks:")
        print("3.update marks:")
        print("4.search Marks:")
        op=int(input("Enter operation: "))
        if op==1:
            m=int(input("Enter the marks to Add:"))
            marks.append(m)
        elif op==2:
            m=int(input("enter marks to Remove:"))
            if m in marks:
                marks.remove(m)
            else:
                print("Marks not Found:")
        elif op==3:
            index=int(input("Enter the index to update:"))
            if 0<=index<len(marks):
                marks[index]=int(input("Enter the new marks:"))
            else:
                print("invalid index")
        elif op==4:
            print("Student Marks:",marks)
        print("Updated marks:",marks)
    # Tuple Operations
    elif choice==2:
        student=("Pooja",17,"CS")
        print("1.Access Student name:")
        print("2.Search an Element:")
        op=int(input("Enter the Operation:"))
        if op==1:
            print("Student Name:",student[0])
        elif op==2:
            item=input("Enter course name to search:")
            if item in student:
                print("Item is found")
            else:
                print("Item is not found")
    # Dictionary Operations
    elif choice==3:
        student={
            "Name":"Shivpooja",
            "Roll NO.":"047",
            "Marks":"100"
        }
        print("1.add new detail:")
        print("2.Delet Record")
        print("3.Search Student:")
        
        op=int(input("Enter Operation:"))
        if op==1:
            key=input("enter new field name:")
            value=input("enter new field value:")
            student[key]=value
        elif op==2:
            key=input("Enter field to delete:")
            if key in student:
                del student[key]
            else:
                print("field is not in Record.")
        elif op==3:
            key=input("Enter the field:")
            if key in student:
                print(key,":",student[key])
            else:
                print("Field is not found.")
    # Set Operations
    elif choice==4:
        set1={"Python","Java","DBMS"}
        set2={"python","c++","DBMS"}
        print("\nSet1:",set1)
        print("set2=",set2)
        print("1.Union")
        print("2.intersection")
        print("3.difference")
        op=int(input("Enter operation:"))
        if op==1:
            print("Union=",set1.union(set2))
        elif op==2:
            print("intersection:",set1.intersection(set2))
        elif op==3:
            print("Differnce=",set1.difference(set2))
        
        print("Updated set1=",set1)
    # Exit
    elif choice==5:
        print("Thank You")
        break
    else:
        print("Invalid Choice plese try again.")




