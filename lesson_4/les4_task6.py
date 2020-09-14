list_number = [int(i) for i in input('Please enter the numbers separated by space:\n').split()]
print(list_number)
counter = 0
for i in range(1, len(list_number) - 1):
    if list_number[i - 1] < list_number[i] > list_number[i + 1]:
        counter += 1
print(counter)
