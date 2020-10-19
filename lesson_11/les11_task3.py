def longest_word(some_str):
    long_word = ''
    for word in some_str.split():
        if len(word) > len(long_word):
            long_word = word
    return long_word


users_str = input('Enter string: ')
print(longest_word(users_str))
