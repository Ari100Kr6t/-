import math
a = float(input())
b = float(input())
c = float(input())
desc = b**2  -  4*a*c
#print(desc)
if (desc > 0):
    print("Уравнение имеет 2 корня:")
    x1 = (-b + math.sqrt(desc)) / (2 * a)
    x2 = (-b - math.sqrt(desc)) / (2 * a)
    print("x1 = ", x1, " x2 = ",x2)
elif (desc == 0):
    print("Уравнение имеет корень:")
    x = -b / (2 * a)
    print("x = ",x)
else:
    print("Уравнение не имеет корней")
