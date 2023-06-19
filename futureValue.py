# Author: Patrick Thrower
# Date: June 19, 2023
# Version: 1.0
#   this is the future value program that takes some input such as inital value
#   and time and interest per amount of time and displays the future value of the
#   interest


def future_value():
    present = float(input('Enter the present value of the account: '))
    interest = float(input('Enter the monthly interest rate from 0%-100%: '))
    months = float(input('Enter the number of months: '))

    future = present * (1 + interest / 100) ** months
    print('$', format(future, '0,.2f'), sep='')
    
future_value()
