# -*- coding: utf-8 -*-
"""reverse2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uWELLutiGJdSoav9O1ZgcBy7Q_Exnpm-
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile reverse1.py
# n = 1234
# reversed_n = 0
# 
# while n != 0:
#     digit = n % 10
#     reversed_n = reversed_n * 10 + digit
#     n //= 10
# 
# print("Reversed Number: " + str(reversed_n))

n = 1234
reversed_n = 0

while n != 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n //= 10

print("Reversed Number: " + str(reversed_n))