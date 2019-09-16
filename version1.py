
password = input("Type in your new password: ",string )
x =password
for i in range(3):
    user_entered= input('Password: ')
    if user_entered is not password:
        print "Wrong Password: "
        user_entered= input('Password: ')
    else:
        print"You are now logged in"
