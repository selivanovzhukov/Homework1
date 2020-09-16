import datetime


day = int(input('Enter day: '))
month = int(input('Enter month: '))
year = int(input('Enter year: '))


def is_date(day: int, month: int, year: int):
    try:
        date = datetime.date(year, month, day)
        print(date)
        return True
    except:
        (print('Incorrect format or date'))


print(is_date(day, month, year))
