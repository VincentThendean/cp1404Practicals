"""
Emails
Estimate: 35 minutes
Start:    15:07
Actual:   35 minutes
End:      15:42
"""


def main():
    user_email = ""
    user_name = ""
    email_dictionary = {}

    user_email = set_email(user_email)

    while user_email != "":
        user_name = auto_set_name(user_email)

        user_name = confirm_name(user_name)

        insert_to_email_dictionary(email_dictionary, user_email, user_name)

        user_email = set_email(user_email)

    get_email(email_dictionary)


def get_email(email_dictionary):
    print()
    for key, value in email_dictionary.items():
        print(f"{value} ({key})")


def insert_to_email_dictionary(email_dictionary, user_email, user_name):
    email_dictionary[user_email] = user_name


def confirm_name(user_name):
    name_check = input(f"Is your name {user_name}? (y/n) ")
    if name_check != "":
        if name_check[0].lower() == "n":
            user_name = input("Name: ")
    return user_name


def auto_set_name(user_email):
    user_name = user_email.split("@")
    user_name = user_name[0]
    user_name = user_name.split(".")
    user_name = " ".join(user_name)
    user_name = user_name.title()
    return user_name


def set_email(user_email):
    user_email = input("Email: ")
    return user_email


main()
