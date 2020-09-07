num = int(input('Please enter the number: '))
s = 0
while num != 0:
    num1 = int(num) % 10
    num = int(num) // 10
    s += num1
print('The sum is:', s)
