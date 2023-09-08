# Author: Patrick Thrower
# Student ID: T00620480
# Date: Sept 6, 2023
# Version: 1.2
# Description: This is a password and username generator program.

first_name = "Roy" #input("Please enter your first name: ")
last_name = "Cabron" #input("Please enter your last name: ")
student_id = "T00123456" #input("Please enter your student ID: ")

# A function that takes the first 3 char of the users first and last name and the last 3 digits of their student id and concats into a username string
def get_login_name():  
    username = first_name[:3] + last_name[:3] + student_id[-3:]
    print(username)

# Simple function that validates that the password is longer than 7 chars and reverse validates that it has a lower and upper case char and a digit
def validate_password():  
    
    x = 4
    while x > 0:
        password = True
        
        enter = input()  # Assigns the users input into password and then passes that into the validate_password function

        if (enter.islower()):
            password = False
            print("Please include a uppercase character")

        if (enter.isupper()):
            password = False
            print("Please include a lowercase character")

        if (len(enter) < 7):
            password = False
            print("Please make the password longer than 7 characters")

        if (enter.isalpha()):
            password = False
            print("Please include a number in your password")

        if(password == False):
            print("\nYou have", x-1, "attempts remaining\n")

        elif (password == True):
            print("\nValid Password")
            break
        x = x - 1   

get_login_name()  # Calls get login function to make the login username
print("\nPlease create a password. A valid password must be at least seven characters in length, Must have at least one uppercase letter, one lowercase letter, and one digit:")
validate_password()