# Digit_name = {
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine",
#     0: "zero"
# }
# num = int(input())
# last_digit = num % 10       # 121 % 10 = 1 (கடைசி digit)
# print(Digit_name[last_digit])




# import random
# alpha = 'HT'
# print(random.choice(alpha))
# print(random.choice(alpha))
# print(len(alpha))

# if False:
#     print("Hello")
# else:
#     print("Hi")

# print("Hello")

# x = int(input())
# if x % 10 == 0:
#     print("Integer")

X = int(input())
x = X % 10
if x == 0:
    print("zero")
elif x == 1:
    print("one")
elif x == 2:
    print("two")
else:    
    print("three")