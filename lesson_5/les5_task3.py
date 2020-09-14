def area(side: int, height: int, figure='triangle'):
    if figure == 'triangle':
        s = 0.5 * side * height
        return s
    else:
        s = side ** 2
        return s


side1 = int(input('Please enter the side: '))
height1 = int(input('Please enter the height: '))
figure1 = input('Please enter the type of figure: triangle or square\n')
print(area(side1, height1, figure1))
