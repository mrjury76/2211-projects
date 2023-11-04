# Author: Patrick Thrower
# Student ID: T00620480
# Date: Nov 4, 2023
# Version: 2.0
# Description: This is a password and username generator program.

#main function that takes input from user and calls both functions
def main():  
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    student_id = input("Please enter your student ID: ")
    get_login_name(first_name, last_name, student_id)  # Calls get login function to make the login username

    print("\nPlease create a password. A valid password must be at least seven characters in length, Must have at least one uppercase letter, one lowercase letter, and one digit:")
    validate_password()

# A function that takes the first 3 char of the users first and last name and the last 3 digits of their student id and concats into a username string
def get_login_name(first_name, last_name, student_id):  
    username = first_name[:3].capitalize() + last_name[:3].capitalize() + student_id[-3:]
    print(username)

# Simple function that validates that the password is longer than 7 chars and reverse validates that it has a lower and upper case char and a digit
def validate_password():
    x = 4
    while x > 0:
        flag = True
        password = input()  # Assigns the users input into password and then passes that into the validate_password function

        if (password.islower()):
            flag = False
            print("Please include a uppercase character")

        if (password.isupper()):
            flag = False
            print("Please include a lowercase character")

        if (len(password) < 7):
            flag = False
            print("Please make the password longer than 7 characters")

        if (password.isalpha()):
            flag = False
            print("Please include a number in your password")

        if (flag == True):
            print("\nValid Password")
            break

        elif(flag == False):
            print("\nYou have", x-1, "attempts remaining\n")
            x -= 1
    
main()