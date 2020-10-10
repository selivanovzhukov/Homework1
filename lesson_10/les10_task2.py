palindrome = str(input('Enter value: '))
value = palindrome[::-1]
if palindrome == value:
    print('It\'s a palindrome')
else:
    print('It isn\'t a palindrome')
