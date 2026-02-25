# Accept three non-negative real numbers as input from the user.
# If the three numbers form the sides of a triangle, print True . 
# If not, print False.

num = [float(input()) for _ in range(3)]
print(num)
if num[0] + num[1] > num[2] and num[0] + num[2] > num[1] and num[1] + num[2] > num[0]:
    print("True")
else:
    print("False")

