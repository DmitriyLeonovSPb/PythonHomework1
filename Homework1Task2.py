a = int(input("Введите число: "))

def minus(a1): #Проверка по нижней границе
    if a1 <= 1:
        return False
    else:
        return True

def big(a1): #Проверка по верхней границе
    if a1 > 100000:
        return False
    else:
        return True

def check(a1): #Проверка на простое
    counter1 = 1
    counter2 = 0
    while counter1 < a1 - 1:
        counter1 = counter1 + 1
        b1 = a1 % counter1
        if b1 == 0:
            counter2 = counter2 + 1
    return counter2
  
if minus(a) == big(a) == True: #Тело
    if check(a) > 0:
        print("Число является составным")
    else:
        print("Число является простым")
else:
    print("Ввод не соответствует условиям задачи")