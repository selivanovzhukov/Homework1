list_of_six = range(100, 206, 6)
for number in list_of_six:
    if number % 5 == 0 and number < 150:
        print(number)
    elif number > 150:
        break
