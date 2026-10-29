import math

# User Inputs
Th = float(input("Please enter the temperature of the house (Farenheit): "))
To = float(input("Please enter the temperature of the outside air (Farenheit): "))
Sa = float(input("Please enter the surface area of the house (ft^2): "))
H = float(input("Please enter the height of the house (ft): "))
# Constants
g = 9.81
Pr = 0.7
v =  0.00001271
k = 0.25

Th = (Th-32)*(5/9)+273.15
To = (To-32)*(5/9)+273.15
Sa = Sa*0.092903
H = H*0.3048

B = 1/To
Ra = (g*B*(Th-To))*((H**3)*(Pr/(v**2)))

Nu = 0.59 * (Ra**k)
h = (Nu*k)/H 

Q = h*Sa*(Th-To)

print("The amount of heat loss is {0:.2f}".format(Q))