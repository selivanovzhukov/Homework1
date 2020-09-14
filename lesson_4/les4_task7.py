num_list1 = [int(i) for i in input('Please enter numbers for the list separated by space:\n').split()]
num_list2 = [int(i) for i in input('Please enter numbers for the list separated by space:\n').split()]
print(f'Exist in both lists ', list(set(num_list1) & set(num_list2)))
print(f'Exist only in first list ', list(set(num_list1) - set(num_list2)))
print(f'Unique for both lists ', list(set(num_list1) ^ set(num_list2)))
