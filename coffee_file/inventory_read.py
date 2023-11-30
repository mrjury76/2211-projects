def main():

    coffee_file = open('inventory.txt', 'r')

    name = coffee_file.readline()
    while name != '':
        qty = float(coffee_file.readline())

        name = name.rstrip('\n')

        print('Name:', name)
        print('Quantity:', qty)

        name = coffee_file.readline()

    coffee_file.close()

main()