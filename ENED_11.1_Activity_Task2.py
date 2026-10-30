num = int(input("Please enter a positive number: "))

while num < 0:
    print("Error: Invalid Input, Try Again")
    num = int(input("Please enter a positive number: "))

factorial = 1

for i in range(num, 1, -1):
    factorial = factorial * i

print("{0}! = {1}".format(num,factorial))