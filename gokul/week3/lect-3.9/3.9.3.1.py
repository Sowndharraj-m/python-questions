# modify the  code so that the output is as below

for i in range(2,11):
    # print(f'1 x [i] = (i)')
    print(f'1 * {i} = {i}')

# output:
'''
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10

'''

# print(f'1 x [i] = (i)')
# [i] → Python thinks this is just text
# (i) → also just text

# print(f"1 x {i} = {i}")
# {i} → Python replaces it with the value of i

"This string contains variables inside {}. Replace them with their values."
# f = format the string

# It allows you to insert:

# Variables

# Calculations

# Expressions