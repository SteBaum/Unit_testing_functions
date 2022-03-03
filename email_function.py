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
    
    password = input("Type your password: ")
    numbers = re.compile('1 2 3 4 5 6 7 8 9 0')
    special_character = re.compile('@ _ ! # $ % ^ & * ( ) < > ? / \ | { } ~ :')
    letters = re.compile('a z e r t y u i o p q s d f g h j k l m w x c v b n A Z E R T Y U I O P Q S D F G H J K L M W X C V B N')
    if (numbers.search(password) == None or special_character.search(password) == None or letters.search(password) == None
    or len(password) < 8):
        print("Password not valid")

    else:
        return "Password has successfully been updated"