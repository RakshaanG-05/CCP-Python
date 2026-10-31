import random

balance = float(input("Enter starting balance: $"))

while balance > 0:
    print("Current balance: ${0:0.2f}".format(balance))
    
    bet = float(input("Enter bet amount: $"))
    while bet <= 0 or bet > balance:
        print("Error: Invalid bet.")
        print("Current balance: ${0:0.2f}".format(balance))
        bet = float(input("Enter bet amount: $"))
        
    choice = input("Enter bet (Under7, Over7, Equal7): ")
    
    Dice1 = random.randint(1, 6)
    Dice2 = random.randint(1, 6)
    dice_sum = Dice1 + Dice2
    
    print("Rolled {0} and {1}. Total: {2}".format(Dice1, Dice2, dice_sum))
    
    if dice_sum < 7:
        outcome = "Under7"
    elif dice_sum > 7:
        outcome = "Over7"
    else:
        outcome = "Equal7"
        
    if choice == outcome:
        if outcome == "Equal7":
            winnings = bet * 4
        else:
            winnings = bet * 1
        balance = balance + winnings
        print("You WON ${0:0.2f}".format(winnings))
    else:
        balance = balance - bet
        print("You LOST ${0:0.2f}".format(bet))
        
    if balance <= 0:
        print("You ran out of money!")
        break
        
    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes" and play_again.lower() != "y":
        break

print("Final balance: ${0:0.2f}".format(balance))