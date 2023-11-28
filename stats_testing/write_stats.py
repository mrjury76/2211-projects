def main():
    character = open("stats.txt", 'w')

    print('Please enter your stats: ')
    stats = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
    for x in range(0, len(stats)):
        output = input(stats[x] + ": ")
        character.write(output + "\n")
    
    character.close()

main()