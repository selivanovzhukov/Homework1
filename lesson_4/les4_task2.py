quantity = 0
summ = 0
product = 1
first_maximum = 0
second_maximum = 0
index_maximum = -1
index = 0
count_even_element = -1
count_odd_element = 0
count_maximum = 0
while True:
    x = int(input('Please enter the number:\n'))
    if x == 0:
        break
    quantity += 1
    summ += x
    product *= x
    if x % 2 == 0:
        count_even_element += 1
    else:
        count_odd_element += 1
    if x > first_maximum:
        first_maximum, second_maximum = x, first_maximum
        count_maximum = 1
        index_maximum = index
    elif x == first_maximum:
        count_maximum += 1
    elif x > second_maximum:
        second_maximum = x
    index += 1
print(f'The quantity of elements is: {quantity}')
print(f'The sum of elements is: {summ}')
print(f'The product of numbers is: {product}')
print(f'The average is: {summ / quantity}')
print(f'The first maximum element is: {first_maximum}')
print(f'The second maximum element is: {second_maximum}')
print(f'The quantity of maximum elements is: {count_maximum}')
print(f'The index of first maximum element is: {index_maximum}')
print(f'The quantity of even elements is: {count_even_element}')
print(f'The quantity of odd elements is: {count_odd_element}')
