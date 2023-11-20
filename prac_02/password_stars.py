def main():
    print("Password must be 10 characters or longer")
    passwordHidden = get_password()
    password_to_stars(passwordHidden)

def password_to_stars(passwordHidden):
    while len(passwordHidden) < 10:
        print("Password must be 10 characters or longer")
        passwordHidden = get_password()
    print('*' * len(passwordHidden))

def get_password():
    passwordHidden = input("Input Password: ")
    return passwordHidden

main()