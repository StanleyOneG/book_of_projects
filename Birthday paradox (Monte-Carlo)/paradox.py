





import datetime, random


def get_birthdays(number_of_birthdays):
    """ Returns a list of number random dates objects for birthdays"""
    birthdays = []
    for i in range(number_of_birthdays):


        start_of_year = datetime.date(2001, 1, 1)


        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays):
    """ Returns the date object of a birthday that occurs
    more than once in the birthday list"""
    if len(birthdays) == len(set(birthdays)):
        return None #All birthdays are unique

    #Compare each birthday to every other birthday
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1 :]):
            if birthday_a == birthday_b:
                return birthday_a #Return the matching birthday


#Display the intro:
print(""" Birthday paradox. Date

The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
""")

#Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True: #Keep asking until the user enters a valid amount`
    print('How many birthdays shall I generate? (Max 150)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 150):
        num_of_days = int(response)
        break #User has entered a valid amount
print()

#Generate and display the birthdays
print('Here are', num_of_days, 'birthdays')
birthdays_for_user = get_birthdays(num_of_days)
for i, birthday in enumerate(birthdays_for_user):
    if i !=0:
        #Display comma for each birthday after the first one
        print(', ', end='')
    month_name = MONTHS[birthday.month - 1]
    date_text = f'{month_name} {birthday.day}'
    print(date_text, end='')
print()
print()

#Determine if there are two birthdays that match
match = get_match(birthdays_for_user)

#Display the result
print('In this simulation, ', end='')
if match != None:
    month_name = MONTHS[match.month - 1]
    date_text = f'{month_name} {match.day}'
    print('multiple people have a birthday on', date_text)
else:
    print('there are no matching birthdays.')
print()

#Run through 100 000 simulations
print('Generating', num_of_days, 'random birthdays 100 000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100 000 simulations.')
simulation_match = 0 # Counting how many simulations have a match
for i in range(100_000):
    #Report the progress every 10 000 simulations
    if i % 10_000 == 0:
        print(i, 'simulations ran...')
    birthdays = get_birthdays(num_of_days)
    if get_match(birthdays) != None:
        simulation_match += 1
print('100 000 simulations completed')

#Display the result
probability = round(simulation_match / 100_000 * 100, 2)
print('Out of 100 000 simulations of', num_of_days, 'people, there was a')
print('matching birthdays in that group', simulation_match, 'times. That means')
print('that', num_of_days, 'people have a', probability, '% chance of')
print('having a matching birthdays in that group.')
print('That\'s probably more than you would think!')
