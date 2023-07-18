

from math import *

print("Welcome to our humble calculator")
print("Choose your operator between:")
print(" + = sum , - = sub , * = mul , / = div")
print("sqrt = Square root , sin = sin , cos = cos , tan = tan , cot = cot , fac = factorial") 

op = input("Plz enter your operator:")

if op == "+" or op == "-" or op == "*" or op == "/": 
    a = float(input("Plz enter your first number:"))
    b = float(input("Plz enter your seconed number:"))
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("Division by zero error")
        else:
            result = a / b
elif op == "sqrt" or op == "sin" or op == "cos" or op == "tan" or op == "cot" or op == "fac":
    a = float(input("Plz enter your first number:"))
    if op == "sqrt":
        result = sqrt(a)
    elif op == "sin":
        result = sin(radians(a))
    elif op == "cos":
        result = cos(radians(a))
    elif op == "tan":
        result = tan(radians(a))
    elif op == "cot":
        result = 1/ tan(radians(a))
    elif op == "fac":
        result = (factorial(int(a)))            
else:
    print("Plz choose operator from your choices")


print ("result=" , result)