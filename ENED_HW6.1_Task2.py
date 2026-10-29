import math

#User Inputs
P = float(input("Please enter the loan amount (principal): "))
A = float(input("Please enter the Annual intrest rate: "))
T = float(input("Please enter the loan term in years: "))

r = A / (12 * 100)
n = T * 12

M = (P * r * (1 + r)**n) / ((1 + r)**n - 1)

print("The monthly payment for the loan is ${0:.2f}".format(M))