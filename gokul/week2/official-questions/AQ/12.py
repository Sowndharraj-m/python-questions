# Accept three integers as input from the user. 
# Print good triplet if one of the three numbers is the sum of the other two, and bad triplet otherwise.

num = [int(input()) for _ in range(3)]
print(num)
if num[0] + num[1] == num[2]:
    print("good triplet")
elif num[0] + num[2] == num[1]:
    print("good triplet")
elif num[1] + num[2] == num[0]:
    print("good triplet")
else:
    print("bad triplet")