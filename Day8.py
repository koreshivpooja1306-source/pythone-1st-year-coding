#Dictionary to add student name and marks from user
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"
students={}
n=int(input("Enter the no. of student:"))
for i in range(n):
    name=(input("Enter the name of student:"))
    marks=int(input("Enter the student marks:"))
    students[name]=marks
for name, marks in students.items():
    grade = get_grade(marks)
    print(name, "Marks:", marks, "Grade:", grade)   
    
    