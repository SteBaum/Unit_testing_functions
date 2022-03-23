import re
import string

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
    
    password = input("Please enter a password: ")
    message = "Password has successfully been updated"

    special_character = ['@ ','_','!','#','$','%', '^', '&', '*', '(', ')', '<', '>', '?', '|','{','}','~',':']
    
    if len(password) < 8:
        print("Password to short, 8 characters minimum")
    elif re.search(str(list(string.digits)), password) is None:
       print("At least one digit required")
    elif re.search(list(string.ascii_letters), password) is None:
        print("At least one letter required")
    elif re.search(str(special_character), password) is None:
            print("At least one speacial character required")
    else:
        return message

# This code should work


