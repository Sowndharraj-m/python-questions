# take a number as input and find the sum of numbers from 1 to that number

x=int(input())
sum=0
for i in range(1,x+13):
    sum = sum + i
print(sum)