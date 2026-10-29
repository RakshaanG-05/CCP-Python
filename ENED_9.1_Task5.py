# Rock, Paper, Scissors
import random

P = float(input("Please enter 1 for One Player or 2 for Two Players: "))

if P == 2:
    P1 = input("Player 1 please pick Rock, Paper, or Scissors: ")   
    P2 = input("Player 2 please pick Rock, Paper, or Scissors: ")

    if P1 == P2:
        print("Tie Game")
    elif (P1 == "Rock" and P2 == "Scissors") or (P1 == "Scissors" and P2 == "Paper") or (P1 == "Paper" and P2 == "Rock"):
        print("Player 1 Wins!!!")
    else:
        print("Player 2 Wins!!!")
else:
    comp_choice = random.randint(1,3)
 # 1 = "Rock"
 # 2 = "Paper" 
 # 3 = "Scissors"

    P1 = float(input("Player 1 please pick the number 1 for Rock, the number 2 for Paper, or the number 3 for Scissors: "))

    if P1 == comp_choice:
        print("Tie Game   Computer chose", comp_choice)
    elif (P1 == 1 and comp_choice == 3) or (P1 == 3 and comp_choice == 2) or (P1 == 2 and comp_choice == 1):
         print("You Win!!! :)  Computer chose", comp_choice)
    else:
        print("You Lose :(  Computer Wins and chose", comp_choice)
