import random

my_number = random.randint(0,9)
guess = input('Guess what number I am thinking from 0 to 9: ')
guess = int(guess)
print (guess)
print (my_number)


while guess != my_number:
    print('Na ah! guess again')
    my_number = random.randint(0,9)
    guess = input('Guess what number I am thinking from 0 to 9: ')
    guess = int(guess)
    print (guess)
    print (my_number)

if guess == my_number:
    print('You guessed correctly!!!')
