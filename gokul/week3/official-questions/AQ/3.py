# Write a program to accept the positive integer n from the user and print the average of all number's factorial

# from 1 to n .

n = int(input("Enter a number: ")) 
fact = 1
for i in range(1,n+1): 
    fact = fact*i
print(fact)

avg = fact/n  
print(avg)