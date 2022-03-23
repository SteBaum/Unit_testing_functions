import re

# More elaborated version (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Tell me your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.') 
    
    else:
        return email


def get_user_name_from_input():
    """ Not empty string. No spaces. """
    user_name = input("Create your user name: ")

    if (" " in user_name or user_name ==""):
        print("Create your user name again: ")

    else:
        return user_name


def get_password_from_input():
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
    
    message = "Password has successfully been updated"
    password = input("Please enter a password: ")
    special_character = ['@ _ ! # $ % ^ & * ( ) < > ? / \ | { } ~ :']
    while True:
        if len(password) < 8:
            print("Your password must be at least 6 characters.")
        elif re.search('[0-9]',password) is None:
            print("Your password must have at least 1 number")
        elif re.search('[A-Z]',password) is None:
            print("Your password must have at least 1 uppercase letter.")
        elif re.search('special_character',password) is None:
            print("Your password must have at least 1 special character ('@ _ ! # $ % ^ & * ( ) < > ? / \ | { } ~ :')")
        else:
            return message
            break


