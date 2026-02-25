# Accept four distinct integers as input from the user.
# Print in ascending order if the four numbers have been entered in ascending order, and print not in ascending order otherwise.

num = [int(input()) for _ in range(4)]
print(num)
if num[0] < num[1] < num[2] < num[3]:
    print("in ascending order")
else:
    print("not in ascending order")

