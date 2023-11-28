def main():
    readfile = open("stats.txt", 'r')
    stats_string = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
    stats = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
    count =  0

    for line in readfile:
        print(stats_string[count] + ": " + line.rstrip('\n'))
        stats[count] = line
        count += 1  
    readfile.close()

    stat_input = int(input('Which stat would you like to check from 1-6: ')) - 1
    print('You have: %d %s' % (int(stats[stat_input]), stats_string[stat_input]))

main()