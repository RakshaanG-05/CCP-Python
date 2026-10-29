# User Inputs
num_res = int(input("Please enter the number of resistors (2 or 3): "))
C = input("Please enter circuit type (Series or Parallel): ")

if num_res == 2 or num_res == 3:
    if C == "Series" or C == "Parallel":
        if num_res == 2:
            R1 = float(input("Please enter value for R1 (ohms): "))
            R2 = float(input("Please enter value for R2 (ohms): "))
            
            if R1 > 0 and R2 > 0:
                if C == "Series":
                    R_Total = R1 + R2
                else:
                    R_Total = 1 / ((1 / R1) + (1 / R2))
                print(f"R_Total = {R_Total:.2f} ohms")
            else:
                print("Error: Resistance must be greater than 0")

        else:  # num_res == 3
            R1 = float(input("Please enter value for R1 (ohms): "))
            R2 = float(input("Please enter value for R2 (ohms): "))
            R3 = float(input("Please enter value for R3 (ohms): "))
            
            if R1 > 0 and R2 > 0 and R3 > 0:
                if C == "Series":
                    R_Total = R1 + R2 + R3
                else:
                    R_Total = 1 / ((1 / R1) + (1 / R2) + (1 / R3))
                print(f"R_Total = {R_Total:.2f} ohms")
            else:
                print("Error: Resistance must be greater than 0")

    else:
        print("Error: Invalid circuit type")

else:
    print("Error: Invalid number of resistors")