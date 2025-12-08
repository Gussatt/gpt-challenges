x = y = n = 0
n = int(input('digite ult.dig.de sua matr.'))
n_ini = n

if (n < 5):
    n = n * 2 + 1
else:
    n = n - 2

if (n > 7):
    n = (n + 1) * 2
else:
    n = n * 2 + 2

if n > 4:
    x = n * 2
    x = n - 1
    if x >= 2:
        x = 4 + n
    else:
        n = n + 1

y = 1
while y < 3:
    if n < 90 and n != 2:
        if n > 2 and n < 21 or n == 22:
            n = n + 20
        elif n < 50:
            n = n + 2
            if n > 5:
                n = n - 1
        else:
            n = 6
    y = y + 1
    n = n + x + y

print("n inicial=", n_ini)
print("n final=", n)