a = 2
b = 2
b2 = 2
c = 6
q = 0
q1 = 4
z = 0
z1 = 9
z2 = 0

def printt(a1, b1, o, o1):
    while o < o1:
        print(a1 + o, "*" , b1, "=" , (a1 + o) * b1,"   ",  end =" ")
        o = o + 1

while z < z1:
    printt(a, b, q, q1)
    print()
    z = z + 1
    b = b + 1

print(" ")

while z2 < z1:
    printt(c, b2, q, q1)
    print()
    z2 = z2 + 1
    b2 = b2 + 1