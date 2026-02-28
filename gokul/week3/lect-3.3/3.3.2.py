# print all odd number between 3 to 30 , using while loop

num = 3
count = 0
while num <=30:
    if (num%2)!=0:
        print(num,end=" ")
        count+=1
    num+=1
print("\n",count)
