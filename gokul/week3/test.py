num = int(input("Enter a number: "))
list1 = [num]
# print(list1)
reverse = 0
while num != 0:
      reverse = reverse * 10 + num % 10
      num = num // 10
list2 = [reverse]
print(list2)

if list1 == list2:
      print("Palindrome")
else:
      print("Not a Palindrome")