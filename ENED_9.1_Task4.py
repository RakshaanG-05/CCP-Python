# User Inputs
T = float(input("Please enter the Tempreture (Celcius): "))
P = float(input("Please enter the Pressue (atm):"))

if T > 355 or P > 0.100:
    print("The state of a Pressurized Water Reactor(PWR) is: Meltdown")
elif T > 345 or P > 0.095:
    print("The state of a Pressurized Water Reactor(PWR) is: Very Severe")
elif T > 335 or P > 0.090:
    print("The state of a Pressurized Water Reactor(PWR) is: Severe")
elif T > 325 or P > 0.085:
     print("The state of a Pressurized Water Reactor(PWR) is: Moderate")
else:
     print("The state of a Pressurized Water Reactor(PWR) is: Normal")