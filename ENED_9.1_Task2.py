# User Input
pH = float(input("Please Enter the pH of the solution (0-14): "))

if 0 <= pH < 7:
    print("Acidic")

else:
    if pH == 7:
        print("Nuetral")

    else:
        if 7 < pH <= 14:
            print("Basic")

        else:
            print ("Invalid Input")
