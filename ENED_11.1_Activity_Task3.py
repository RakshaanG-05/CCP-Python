num = int(input("How many Fibonacci Numbers do you want? "))

while num <= 0:
    print("Error: Invalid Input, Try Again")
    num = int(input("How many Fibonacci Numbers do you want? "))

fib = 0
fib1 = 1
iteration = int((num / 2) + 1)

print("Fibonacci sequence with {0} terms: ".format(num))

for i in range(iteration, 1, -1):
    print("{0}".format(fib))
    print("{0}".format(fib1))
    fib = fib + fib1
    fib1 = fib + fib1