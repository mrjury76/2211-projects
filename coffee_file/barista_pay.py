def main():
    NUM_EMPLOYEE = 4 #declaring global var for the number of employees

    #making 2 lists for the hours worked and the employees
    hours_worked = [0] * NUM_EMPLOYEE
    gross_pay = [0] * NUM_EMPLOYEE
    employees = [0] * NUM_EMPLOYEE

    #loop to assign the hours to the employees
    for people in range(len(employees)):
        print(f'Employee number {people+1}\'s hours: ', end = '')
        hours_worked[people] = input()

    pay_rate = input('What is the pay rate?: ')

    #looping the hours times the pay for gross pay
    for index in range(len(gross_pay)):
        gross_pay[index] = int(hours_worked[index]) * int(pay_rate)
        print(f'Emp #{index+1}\'s gross pay is: ${gross_pay[index]}')

    # print(gross_pay)

main()
