# Python Programming

password = raw_input("Type in your new password: ")
user_password = password

for i in range(3):
    enter_password = raw_input("Enter Password: ")
    if enter_password == user_password:
        print"Password is correct "
        break

    elif enter_password == user_password:
        print"Password is not correct"

    elif i == 2:
        print"Account is Locked"

