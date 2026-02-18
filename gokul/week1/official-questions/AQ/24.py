# Accept a two digit number as input and print the sum of its digits. 
# What about a three digit number?

num = int(input())
print(num // 10 + num % 10)

# 123
# 12 // 10 = 1
# 12 % 10 = 2
# 1 + 2 = 3
