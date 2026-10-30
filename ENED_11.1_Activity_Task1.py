import random

num_flips = int(input("Please enter how many times you want to flip the coin: "))

if num_flips > 0:
    flip = random.randint(0,1)

    H = 0
    T = 0
    iteration = num_flips

        while n > 0:
            if flip == 1:
                H = H + 1
            else:
                T = T + 1
            iteration = iteration - 1
        
        H_Percent = (H/num_flips) * 100
        T_Percent = (T/num_flips) * 100
    
        print("After {0} flips, The coin landed Heads {1:0.2f} percent the time and landed Tails {2:0.2f} percent of the time".format(num_flips, H_Percent, T_Percent))
else:
    print("Error: Invalid Input")
                