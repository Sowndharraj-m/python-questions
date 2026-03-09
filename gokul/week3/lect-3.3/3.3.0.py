# take a string as input and print it back by removing the first and last character of the input string

input_string = input("Enter a string: ")
x  = input_string[::-1] 
# print(x)  # Print the reversed string

print(x[1:len(x)])  # Remove first and last character of reversed string
        
