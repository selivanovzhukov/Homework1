def prime(n):
    x = 2
    while x < n:
        if n % x != 0:
            x += 1
            continue
        else:
            return False
    return True


prime_n = []
for i in range(1, 1000):
    if prime(i):
        prime_n.append(i)
    else:
        continue

print(prime_n)
