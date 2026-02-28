# start, end = "C3","E5"
# pos = 'ABCDEFGH'
# start_horiz = pos.index(start[0])-----> 2
# start_vert = int(start[1])------>3
# end_horiz = pos.index(end[0])-------->4
# end_vert = int(end[1])------->5
# print(start_horiz, start_vert, end_horiz, end_vert)

# if abs(start_horiz - end_horiz) == abs(start_vert - end_vert):
#  print('YES')
# else:
#  print('NO')

name = "gokul"
if name.isalpha():
  print("valid")
else:  
 print("invalid")