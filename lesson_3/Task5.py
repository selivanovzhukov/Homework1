import random
number = random.randint(1, 10)
chances = 1
while chances <= 3:
    guess = int(input('Enter your number (between 1 and 10): '))
    if guess == number:
        print('Congratulations YOU WON!!!')
        break
    elif guess != number:
        print(f'{guess} is wrong number, try again')
        chances += 1
else:
    print('YOU LOSE!!! The number is', number)