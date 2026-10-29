import math

k1 = float(input("Please enter the first spring constant(N/m): "))
k2 = float(input("Please enter the second spring constant(N/m): "))
F = float(input("Please enter the total force(N): "))
Config = input("Please enter the configuration (Series or Parallel): ")

if k1 > 0 and k2 > 0 and F > 0:
    if Config == "Series":
        keq = (k1*k2) / (k1+k2)
        F1 = F
        F2 = F
        x1 = F1/k1
        x2 = F2/k2
        xT = x1 + x2
        print(
            "The values are:",
            f"k equivalent: {keq} (N/m)",
            f"The force on spring one: {F1} (N)",
            f"The force on spring 2: {F2} (N)",
            f"The distance spring one is compressed: {x1} (m)",
            f"The distance spring 2 is compressed: {x2} (m)",
            f"The total distance the system is compressed: {xT} (m)",
            sep="\n")
    else:
        if Config == "Parallel":
            keq = k1 + k2
            xT = F/keq
            x1 = xT
            x2 = xT
            F1 = k1*x1
            F2 = k2*x2
            print(
                "The values are:",
                f"k equivalent: {keq} (N/m)",
                f"The force on spring one: {F1} (N)",
                f"The force on spring 2: {F2} (N)",
                f"The distance spring one is compressed: {x1} (m)",
                f"The distance spring 2 is compressed: {x2} (m)",
                f"The total distance the system is compressed: {xT} (m)",
                sep="\n")
        else:
            print("Error: Invalid Configuration")
else:
    print("Error: Invalid Inputs")
