"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

nameUser = str(input("Enter name: "))
print("(H)ello \n(G)oodbye \n(Q)uit")
choiceMenu = str(input(">>> "))
while choiceMenu != 'Q':
    if choiceMenu == 'H':
        print(f'Hello {nameUser}')
    elif choiceMenu == 'G':
        print(f'Goodbye {nameUser}')
    else:
        print('Invalid Choice')
    print("(H)ello \n(G)oodbye \n(Q)uit")
    choiceMenu = str(input(">>> "))
print('Finished')