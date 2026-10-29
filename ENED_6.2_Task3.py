import math

# User Inputs
M = float(input("Please enter the maximum allowable SPL (dB):  "))
R = float(input("Please enter the reference pressure (Pa):  "))
V = float(input("Please enter the particle velocity (m/s):  "))
# Constants
P = 0.000001
S = 190

P = R*10**(S/20)
I = P * V

print("The sound intensity in (W/m^2) is {0:.2f}".format(I))