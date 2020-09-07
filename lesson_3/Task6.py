print('The chessboard have 8 vertical cells (Y) and 8 horizontal cells (X). Please enter cell coordinates:')
x1 = int(input('Enter x1 coordinate: '))
y1 = int(input('Enter y1 coordinate: '))
x2 = int(input('Enter x2 coordinate: '))
y2 = int(input('Enter y2 coordinate: '))
if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or \
        (abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
    print("YES")
else:
    print("NO")
