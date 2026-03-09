# find the factorial of a number using while loop, take number n as input


4!= 4 * 3 * 2 * 1 

n = int(input("Enter a number: "))
factorial = 1
count = 1       
while count <= n: 
    factorial = factorial * count 
    count += 1  
print(factorial)
