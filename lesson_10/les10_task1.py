file_name = input('Create new file: ')
with open(file_name, 'w') as f:
    while True:
        some_string = input('Input string: ')
        if some_string == '':
            break
        f.write(some_string + '\n')
