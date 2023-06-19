# Author: Patrick Thrower
# Student ID: T00620480
# Date: June 19, 2023
# Version: 1.0
#   this is the future value program that takes some input such as inital value
#   and time and interest per amount of time and displays the future value of the
#   compounding interest


def future_value():
    present = float(input('\nEnter the present value of the account: '))
    interest = float(input('Enter the monthly interest rate from 0-100%: '))
    months = float(input('Enter the number of months: '))

    future = present * (1 + interest / 100) ** months
    change = future - present

    print('\nWith an initial value of $', format(present, '0,.2f'), ', over a period of ', format(months, '0,.0f'), 
        ' months, and an interest rate of ', interest, '% per month, the future value of your account will be: ', sep='')
    print('$', format(future, '0,.2f'), sep='')
    print('Thats an increase of $', format(change, '0,.2f'), '!\n', sep = '')
    
future_value()

#test test