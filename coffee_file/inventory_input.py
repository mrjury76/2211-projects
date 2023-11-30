def main():

    outfile = open("inventory.txt", 'a')
    again = 'y'

    while (again == 'y'):
        name = input("Name of the coffee: ")
        weight = float(input("How much does the coffee weigh: "))

        outfile.write(name + "\n")
        outfile.write(str(weight) + "\n")

        again = input('Would you like to input another item? Y = Yes')

    outfile.close()

main()