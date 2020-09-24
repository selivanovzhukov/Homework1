def word_list(function):
    func = function()
    print(func.split())
    return func


@word_list
def word_str():
    return input('Enter string: ')
