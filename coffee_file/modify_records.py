import os # Needed for the remove and rename functions

def main():
    found = False
    # Get the search value and the new quantity.
    search = input('Enter a description to search for: ')
    new_qty = int(input('Enter the new quantity: '))
    # Open the original coffee.txt file.
    coffee_file = open('inventory.txt', 'r')
    # Open the temporary file.
    temp_file = open('temp.txt', 'w')
    # Read the first record's description field.
    descr = coffee_file.readline()
    # Read the rest of the file.
    while descr != '':
    # Read the quantity field.
        qty = float(coffee_file.readline())
    # Strip the \n from the description.
        descr = descr.rstrip('\n')
    # Write either this record to the temporary file,
    # or the new record if this is the one that is
    # to be modified.
        if descr == search:
    # Write the modified record to the temp file.
            temp_file.write(descr + '\n')
            temp_file.write(str(new_qty) + '\n')

    # Set the found flag to True.
            found = True
        else:
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')
        descr = coffee_file.readline()
    coffee_file.close()
    temp_file.close()
    
    os.remove('inventory.txt')
    os.rename('temp.txt', 'inventory.txt')
    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')
main()