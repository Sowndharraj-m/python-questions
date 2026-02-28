# take a number as input and find the sum of numbers from 1 to that number

num = int(input("Enter a number: "))
sum = 0

while (num!=0):
    sum = sum + num
    num -= 1
print(sum)

num = int(input("Enter a number: "))
sum = 0

for i in range(1, num + 1):
    sum = sum + i
print(sum)
