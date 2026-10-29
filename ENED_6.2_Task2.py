import math

# User Inputs
V = float(input("Please enter the fluid velocity (mph): "))
L = float(input("Please enter the typical length (in): "))
U = float(input("Please enter the dynamic viscosity of the fluid (lb/(in*s)): "))
P = float(input("Please enter the fluid density (lb/(in^3)): "))

V1 = V * 5280 * 12 / (60 * 60)
Re = P * V1 * L / U

print("The Reynolds Number is {0}".format(Re))

