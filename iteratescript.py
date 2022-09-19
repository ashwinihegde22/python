print("Printing current and previous number and their sum in  range(10)")
pn = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = pn + i
    print("Current Number", i, "Previous Number ", pn, " Sum: ", pn + i)
    
    pn = i
