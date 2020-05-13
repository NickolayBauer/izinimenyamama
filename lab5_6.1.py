from lab5_6 import sl
def n1():
    print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % discr)

    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        print("Корней нет")

def n2():
    a = float(input("a = "))
    x1 = - math.sqrt(a)
    x2 = math.sqrt(a)
    print("x1 = ", x1, "x2 = ", x2)

def n3min():
    a = float(input("a = "))
    b = float(input("b = "))
    x1 = 0
    x2 = b/a
    print("x1 = ", x1, "x2 = ", x2)

def n3pl():
    a = float(input("a = "))
    b = float(input("b = "))
    x1 = 0
    x2 = -b / a
    print("x1 = ", x1, "x2 = ", x2)
n3pl()