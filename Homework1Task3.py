from random import randint 
num = randint(0, 1000)
print(num)
a = 10
counter = 0
while counter < a:
    print("Осталось попыток: ", a - counter)
    b = int(input("Введите число: "))
    if b == num:
        print("Вы угадали")
        break
    else:
        print("Вы не угадали")
        if b > num:
            print("Введите поменьше")
        else:
            print("Введите побольше")
        counter = counter + 1