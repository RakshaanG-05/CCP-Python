import math

# User Inputs
A = float(input("Please enter the angle (Only the number): "))
U = input("Please enter what type of units you used (Degrees or Radians): ")

if U == "Degrees" or U == "Radians":
    if U == "Radians":
        A = round(A * (180 / math.pi))

    if A < 0 or A > 360:
        print("Error: Invalid Input")
    else:
        if 0 <= A <= 90:
            Q = 1
            Y = (math.sin(math.radians(A))**2) / (1 - (math.sin(math.radians(A))**2))
        elif A <= 180:
            Q = 2
            Y = math.sqrt(1 - (math.cos(math.radians(A))**4))
        elif A <= 270:
            Q = 3
            Y = -math.sqrt(1 + (math.tan(math.radians(A))**2)) / math.tan(math.radians(A))
        else:
            Q = 4
            Y = -1 / math.sqrt(1 - (math.sin(math.radians(A))**2))

        print(f"Quadrant: {Q}, Y({A:.0f} deg) = {Y:.2f}")

else:
    print("Error: Invalid Unit")