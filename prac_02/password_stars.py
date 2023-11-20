def main():
    print("Password must be 10 characters or longer")
    hidden_password = get_password()
    password_to_stars(hidden_password)

def password_to_stars(hidden_password):
    while len(hidden_password) < 10:
        print("Password must be 10 characters or longer")
        hidden_password = get_password()
    print('*' * len(hidden_password))

def get_password():
    hidden_password = input("Input Password: ")
    return hidden_password

main()