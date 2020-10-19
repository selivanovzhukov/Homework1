def hide_email(email):
    part1 = email.split('@')[0][:-3]
    part2 = email.split('@')[1][3:]
    return part1 + '***' + '@' '***' + part2


some_email = input('Enter your e-mail: ')
print(hide_email(some_email))
