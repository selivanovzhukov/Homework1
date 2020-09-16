var_dict = {'first_name': 'James', 'second_name': 'Bond', 'code_name': '007', 'age': None}


def remove_empty(var_dict: dict) -> dict:
    var_dict = {key: value for key, value in var_dict.items() if value is not None}
    return var_dict


print(remove_empty(var_dict))
