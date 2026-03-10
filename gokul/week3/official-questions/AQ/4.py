# Write a program to accept the positive integer n from the user and print counting of numbers which are not

# prime from 1 to n.

n = int(input("Enter a number: "))
count = 0

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
        print(num,end = ' ')

print("\n",count)   
