# Program to find all prime numbers from 1 to 10

for num in range(9):
    if num <= 1:
        continue
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number")