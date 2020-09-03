if __name__ == "__main__":
    y = abs(int(input('Please enter your year: ')))
    print('Your year is:', y)
    if (y % 4 == 0) and (y % 100 != 0) or (y % 400 != 0):
        print('Yes')
    else:
        print('No')
