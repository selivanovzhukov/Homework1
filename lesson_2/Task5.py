if __name__ == "__main__":
    def sign(x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0
    x = int(input('Please enter x value: '))
    print(sign(x))
