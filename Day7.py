# To check the password is strong or not
password=(input("Enter the password:"))
# First set all values as Flase
has_upper=False
has_lower=False
has_digit=False
has_special=False

# To check Each Character in string as it has atleast one property of it
for ch in password:
    if ch.isupper():
        has_upper=True
    elif ch.islower():
        has_lower=True
    elif ch.isspecial():
        has_special=True
    else:
        has_digit=True

# To check all values are true or not
if (len(password)>=8)and has_upper and has_lower and
has_digit and has_special:
    print("Password is strong.")
else:
    print("Password is not strong.")
    print("Required things in Strong Password:")
    print("At least 8 characters.")
    print("It should have a upper case and lower case character")
    print("It should have at least one the digit as character")
    print("It should have at least one special character")





 