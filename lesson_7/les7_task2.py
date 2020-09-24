temp_value = int(float(input('Please enter the value:\n')))
temp_unit = input('Please enter the type:\n')


def temp_calc(temp_value, temp_unit):
    if temp_unit == 'K':
        k = temp_value
        c = temp_value + 273.15
        f = int(float((temp_value + 459.67) / 1.8))
        print(f'The temperature in Kelvins is {k}, in Celsius is {c}, in Fahrenheits is {f}.')
    elif temp_unit == 'C':
        c = temp_value
        k = temp_value - 273.15
        f = int(float(temp_value - 32)) / 1.8
        print(f'The temperature in Celsius is {c}, in Kelvins is {k}, in Fahrenheits is {f}.')
    elif temp_unit == 'F':
        f = temp_value
        k = int(float(temp_value + 459.67) / 1.8)
        c = int((temp_value - 32) / 1.8)
        print(f'The temperature in Fahrenheits is {f}, in Kelvins is {k}, in Celsius is {c}.')
    else:
        print('')

temp_calc(temp_value, temp_unit)
