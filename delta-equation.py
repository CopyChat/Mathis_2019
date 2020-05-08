from math import sqrt

print("Bonjour ! Nous allons resoudre une equation du second degré")

a = int(input("Quelle est la valeur de a ?"))
b = int(input("Quelle est la valeur de b ?"))
c = int(input("Quelle est la valeur de c ?"))


print(f'你输入的方式是:\n{a:g}x^2 + {b:g}x + {c:g} = 0')

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-sqrt(delta)-b)/(2*a)
    x2 = (sqrt(delta)-b)/(2*a)
    print("Les solutions de l'équation sont", x1, "et", x2)

elif delta < 0:
    print("L'équation n'a pas de solution dans R")

elif delta == 0:
    x1 = x2 = -b / (2*a)
    print("L'équation a une solution double :", x1)











