import math

#User Inputs
m = float(input("Please enter the mass of the object (kg): "))
Vi = float(input("Please enter the initial velocity (m/s): "))
Vf = float(input("Please enter the final velocity (m/s): "))

W = 1/2 * m * (Vf**2 - Vi**2)

print("The work done in joules is {0:.2f}".format(W))