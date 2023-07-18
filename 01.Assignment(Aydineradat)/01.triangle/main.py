print("this program shows you three side of triangle you introduce can be a triangle or not")

a = float(input("Plz enter first sides length"))
b = float(input("Plz enter seconed sides length"))
c = float(input("Plz enter third sides length"))

if a + b > c and c + a > b and b + c > a:
    print("yeah it a Triangle")
else:
    print("no it is not a triangle")