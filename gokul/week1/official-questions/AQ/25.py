# Accept a positive integer as input and print True 
# if it is a perfect square and False otherwise. For example, 
# if the input is 25 , then you must print True . 
# If the input is 15 , then you must print False

num = int(input())
print((num ** 0.5).is_integer())

5 ** 2     # 25  (5-ஐ square செய்)
25 ** 0.5  # 5.0 (25-ஐ square root செய்)

** 2   = மேலே ஏறு (square)
** 0.5 = கீழே இறங்கு (square root)

25 ** 0.5 = ?  →  ? × ? = 25  →  ? = 5

0.5 = 1/2, இது 2-ன் தலைகீழ் (inverse). அதனால்:

** 2 → square (பெருக்கு)
** 0.5 (i.e., ** 1/2) → square root (மீட்டுக்கொண்டு வா)