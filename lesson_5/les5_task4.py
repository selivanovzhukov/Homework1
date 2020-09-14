random_list = list(range(0, 15))
print(random_list)
for i in range(len(random_list)):
    if random_list[i] % 2 != 0:
        random_list[i] = 0
print(random_list)
print(random_list.count(0))
