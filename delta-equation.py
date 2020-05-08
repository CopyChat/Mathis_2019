from math import sqrt

print("Bonjour ! Nous allons resoudre une equation du second degré")

a = int(input("Quelle est la valeur de a ?"))
b = int(input("Quelle est la valeur de b ?"))
c = int(input("Quelle est la valeur de c ?"))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-sqrt(delta)-b)/(2*a)
    x2 = (sqrt(delta)-b)/(2*a)
    print("Les solutions de l'équation sont", x1, "et", x2)

elif delta < 0:
    print("L'équation n'a pas de solution dans R")

elif delta == 0:
    x1 = x2 = -b / (2*a)
    print("Léquation a une solution double :", x1)











