n = int(input('Enter the N <= 9: '))
if n <= 9:
    string = ''
    for i in range(1, n+1, 1):
        string += str(i)
        print(string)
if n <= 0:
    print('The number is to low')
else:
    print('The number is to big')
