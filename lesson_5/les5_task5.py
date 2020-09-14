a = int(input('Enter square side value: '))
a = float(a)


def square(a):
    p = a * 4
    s = a ** 2
    d = a * (2 ** 0.5)
    return {p, s, d}


print(square(a))
