a = int(input('Please enter A value:'))
b = int(input('Please enter B value:'))
if a < b:
    for i in range(a, b + 1, 1):
        print(i)
elif a > b:
    for i in reversed(range(b, a + 1, 1)):
        print(i)
