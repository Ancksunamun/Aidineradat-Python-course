
a = 0 
b = 0
c = 1

n = int(input("Plz enter the number of fibonachi equation members you wanna see: "))

while n != 0:
    
    print(" " , c , end="")
    a = b
    b = c
    c = a + b
    n -= 1