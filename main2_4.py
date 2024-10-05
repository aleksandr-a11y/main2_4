numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 0 or i == 1:
        continue
    in_primes = False
    for j  in range(2, i):
        if i % j == 0:
            in_primes = True
            break
    if in_primes == False:
        primes.append(i)
    else:
        not_primes.append(i)
print("Primes: ", primes)

print("Not Primes: ", not_primes)

