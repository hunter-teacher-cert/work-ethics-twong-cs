import random

#secret number chosen randomly
number = random.randint(1,100)

#prompt user to guess number
print('\nI am thinking of a number between 1 and 100, inclusive.')
print('Can you guess what it is?')
print('\nType in a number: ')
guess = input()

#compares user guess to secret number
if guess > number:
    difference = guess - number
elif number > guess:
    difference = number - guess
elif number == guess:
    difference = 0
    print('\nCongrats! You guessed the secret number.')

#provides feedback on user guess
print('\nYour guess was: ' + str(guess))
print('The number I was thinking of was: ' + str(number))
print('You were off by: ' + str(difference))
