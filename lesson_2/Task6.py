tup = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
x = abs(int(float(input('Enter the number: '))))
if x in tup:
    print(f'The number is in the tuple with index = [{tup.index(x)}]')
else:
    print('There is no such element in the tuple')
