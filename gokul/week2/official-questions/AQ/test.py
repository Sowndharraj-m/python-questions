Digit_name = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    0: "zero"
}

num = int(input())
last_digit = num % 10       # 121 % 10 = 1 (கடைசி digit)
print(Digit_name[last_digit])

