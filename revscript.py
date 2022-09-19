n = 1234
rev_n = 0

while n != 0:
    digit = n % 10
    rev_n = rev_n* 10 + digit
    n //= 10

print("Reversed Number: " + str(rev_n))
