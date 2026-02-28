# take year of birth (YOB) as input,
# print the current age of the person and also print if the person is eligible to vote or not


# HINT : subtract current year from YOB

current_age = 2026 - int(input())
print(current_age)
if current_age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")