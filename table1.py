#multiplication
num = int(input('table you want to write  here:'))

s_range = int(input('write the number from where to start:'))
e_range = int(input('write the end of the number you need:'))
print()
print(' here is the table of', num)
for i in range(s_range, e_range + 1):
   print(num, 'x', i, '=', num*i)
