# login System For User
correct_password="Pooja@1306"
attempts=1
for attempts in range(3):
    user_password=input("Enter the password:")
    if correct_password==user_password:
        print("Login Successful.")
        break
    else:
        print("Login Failed:")
else:
    print("You got maximum time login, login Failed.")