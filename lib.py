def sl():
    a = float(input("Введите первое слогаемое : "))
    b = float(input("Введите второе слогаемое : "))
    c = a + b
    print("Ответ : ", c)

def vch():
    a = float(input("Введите уменьшаемое : "))
    b = float(input("Введите вычитаемое : "))
    c = a - b
    print("Ответ : ", c)
def delen():
    a = float(input("Введите делимое : "))
    b = float(input("Введите делитель : "))
    if b == 0:
        print("Извините, но Вы тупой! Делить на 0 нельзя.")
        return
    c = a/b
    print("Ответ : ", c)
def umn():
    a = float(input("Введите первый множитель : "))
    b = float(input("Введите второй множитель : "))
    c = a*b
    print("Ответ : ", c)
