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
    special_character = ['@ ','_','!','#','$','%', '^', '&', '*', '(', ')', '<', '>', '?', '|','{','}','~',':']
    password = input("Please enter a password: ")
        if (len(password) < 8: or re.search('[0-9]',password) is None or re.search('[a-z]',password) is None\
        or  re.search(special_character ,password) is None):
            print("Your password is incorrect")
        else:
            return message


