# Author: Patrick Thrower
# Student ID: T00620480
# Date: October 29, 2023
# Version: 2.0
#   this is the future value program that takes some input such as inital value, 
#   time, and interest per amount of time and displays the future value of the
#   compounding interest


def main():
    while True:
        present_str = input('\nEnter the present value of the account: ')
        interest_str = input('Enter the monthly interest rate from 0-100%: ')
        months_str = input('Enter the number of months: ')

        if present_str.isnumeric() and interest_str.isnumeric() and months_str.isnumeric():
            present = float(present_str)
            interest = float(interest_str)
            months = float(months_str)
            
            if present > 0 and interest > 0 and interest <= 100 and months > 0:
                break
            else:
                print("\nPlease enter positive values within the specified range.")
        else:
            print("\nPlease enter valid numeric values.")

    future = future_value(present, interest, months)  # Processing the inputs with the actual function
    change = future - present  # Calculating the change in the account

    print('\nWith an initial value of $', format(present, '0,.2f'), ', over a period of ', format(months, '0,.0f'),   # Output of the program
        ' months, and an interest rate of ', interest, '% per month, the future value of your account will be: ', sep='')
    print('$', format(future, '0,.2f'), sep='')
    print('Thats an increase of $', format(change, '0,.2f'), '!\n', sep = '')
    
def future_value(present, interest, months):  # Function that receives the 3 inputs 
    future = present * (1 + interest / 100) ** months  # Formula to calculate the future value of the inputs
    return future   # Output

main()   # Calling the main function