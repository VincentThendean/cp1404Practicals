print("Password must be 10 characters or longer")
passwordHidden = input("Input Password: ")

while len(passwordHidden)<10:
    print("Password must be 10 characters or longe r")
    passwordHidden = input("Input Password: ")

print('*'*len(passwordHidden) )