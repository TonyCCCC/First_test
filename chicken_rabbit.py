from sympy import symbols, solve
from math import modf

def isInt(inp):
    while True:
        try:
            inp = float(inp)
            dec = modf(inp)
            if dec[0] == 0:
                return inp
                break
            else:
                inp = input("Input Error! Try Again: ")
        except:
            inp = input("Input Error! Try again: ")

head = input("Input heads: ")
head = isInt(head)
foot = input("Input foot: ")
foot = isInt(foot)

result = {}
x = symbols('x')
y = symbols('y')
result = solve([x + y - head, 2 * x + 4 * y - foot], [x, y])
print(result)
if result[x] >= 0 and result[y] >= 0 and modf(result[x])[0] + modf(result[y])[0] == 0:
    print("Chicken: %d, rabbits: %d."%(result[x], result[y]))
else:
    print("Unsolvable!")