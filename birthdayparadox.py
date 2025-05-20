import datetime, random

def getBirthdays(numberOfBirthdays):
    """"Returns a list of number random date objects for birthdays."""
    birthdays = []

    for i in range(numberOfBirthdays):
        #Year is unimportant as long as birthdays have same year
        startOfYear = datetime.date(2001, 1, 1)

        #Get random day into year:

        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """"Returns the birthday that occurs moret than once in the birthdays list"""
    if len(birthdays) == len(set(birthdays)):
        return None #all birthdays are unique, so return none
    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA   #returns the matching birthday.
            

#display the intro
print('''ssuup it is John bringing you the birthday paradox
 The birthday paradox show us that in a group of N people,the
 odds that two peeps have the same birthday is large my G          
       
''')   

#tuple of months in order:
MONTHS =('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:# Keep asking until the user enters a valid amount.
    print('How many birthdays shall i generate?(max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBdays = int(response)
    break # User entered valid amount
print()

#Generatte and display birthdays:
print('Here are', numBdays, 'birthdays:')

birthdays = getBirthdays(numBdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        #display comma for each birthday after the first birthday
        print(', ' , end='' )


    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')

print()
print()


#determine if two birthdays match
match = getMatch(birthdays)

#display results
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple peeps have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# run thru 100,000 simulations
print('Generating', numBdays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations')

simMatch = 0 #No of simullations that had matching birthdays in them
for i in range(100_000):
    # report on progress every 10,000 simulation
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBdays) 
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1

print('100,000 simulations run') 

#Diplay simulations results:
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBdays, 'people,there was a')
print('Matching birthday on that group', simMatch, 'times.This means')
print('that', numBdays, 'people have a', probability, '%chance of')
print('having a matching birthday in the group')
print('That\'s probably more than you think ')
        

