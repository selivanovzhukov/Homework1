if __name__ == "__main__":
    v = int(input('Please enter Vasya\'s velocity: '))
    print('Vasya\'s velocity is:', v)
    t = int(input('Please enter Vasya\'s travel time: '))
    print('Vasya\'s travel time is:', t)
    s = int(v * abs(t))
    if v > 0 and s >= 100:
        print('Vasya is riding in the right direction 👍', '\nVasya\'s position:', s)
    elif v <= 0 and s <= 100:
        print('Vasya is going in wrong direction!')
    else:
        print('Vasya\'s position is:', s)
