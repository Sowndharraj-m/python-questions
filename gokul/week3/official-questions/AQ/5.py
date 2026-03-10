# Write a program to accept the string s from the user and print all alphabets in one line separated by , before

# first occurrence of vowels .
s = input("Enter a string: ")
vowels = "aeiouAEIOU"

for char in s:
    if char in vowels:
        break
    print(char, end=",")