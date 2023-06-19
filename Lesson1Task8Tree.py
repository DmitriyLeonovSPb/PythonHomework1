a = int(input("Введите высоту ёлки: "))
len1 = 1 + 2 * (a - 1)
arra1 = [" "] * len1
q = a - 1
arra1[q] = "*"
print(' '.join(arra1))
q1 = q
while q < len1 - 1:
    q = q + 1
    q1 = q1 - 1
    arra1[q] = "*"
    arra1[q1] = "*"
    print(' '.join(arra1))