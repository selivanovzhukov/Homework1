x = int(float(input('Enter first day distance: ')))
y = int(float(input('Enter required distance: ')))
i = 1
while x <= y:
    x *= 1.1
    i += 1
print(f'At the {i} day distance will be {y}km')
