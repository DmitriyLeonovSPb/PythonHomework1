a = input("Введите сторону A: ")
b = input("Введите сторону B: ")
c = input("Введите сторону C: ")

def isfloat(value):   #проверка на ввод числа
    try:
        float(value)
        return True
    except ValueError:
        return False

def diverse1(a1, b1, c1): #проверка на разные стороны
    if (a1 != b1) and (b1 != c1) and (c1 != a1):
        return True
    else:
        return False

def equilateral1(a1, b1, c1): #проверка на равные стороны
    if (a1 == b1) and (b1 == c1) and (c1 == a1):
        return True
    else:
        return False        

def comparison1(a1, b1, c1): #сравнение суммы двух чисел с третьим
    if a1 + b1 > c1:
        return True
    else:
        return False

if isfloat(a) == isfloat(b) == isfloat(c) == True: #тело
    a = float(a)
    b = float(b)
    c = float(c)
    diverse = diverse1(a, b, c)
    equilateral = equilateral1(a, b, c)
    if comparison1(a, b, c) == comparison1(c, b, a) == comparison1(c, a, b) == True:
        print("Треугольник существует")
        if diverse == True:
            print("Треугольник разносторонний")
        else:
            if equilateral == True:
                print("Треугольник равносторонний")
            else:
                print("Треугольник равнобедренный")
    else:
        print("Треугольник не существует")
else:
    print("Введены не числа, повторите попытку ввода")