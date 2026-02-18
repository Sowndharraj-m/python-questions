# Consider the following code block:

x=int(input())

# What happens if the input is 1.23 ? Execute and observe the output.
# Why do you think this is happening?
# ValueError: invalid literal for int() with base 10: '1.23'
#Reason : The int() function can only convert strings that represent whole numbers (integers) to integers. It cannot convert strings that represent decimal numbers (floats) to integers.       