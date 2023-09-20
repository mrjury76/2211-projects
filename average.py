import random


dice = input("Please enter the number of sides the dice has: ")
n = int(input("Please enter the number of dice being rolled: "))

def average(n, dice): 
    million = 1000000
    average = 0

    for x in range(million):
        average += random.randint(1, int(dice))
    average = average * n
    average = average / million
    print("The average of {n} D{d} is {output:.2f}".format(n =n, d = dice, output = average))

def advantage():
    million = 1000000
    average = 0

    for i in range(million):
        x = random.randint(1, 20)
        y = random.randint(1, 20)
        advantage = max(x, y)
        average += advantage
    average = average / million
    print("The average of 2d20 rolled with advantage is: {k:.2f}".format(k = average))

def upper_roll(n, dice):
    output = int(dice) * int(n)
    print("Upper Roll: ", output)

def lower_roll(n):
    output = 1 * int(n)
    print("Lower Roll: ", output)

average(n, dice)
upper_roll(n, dice)
lower_roll(n)