x = y = n = 0

n = int(input('digite ult.dig.de sua matr.'))
n_ini = n

if (n > 5):
    n = n * 3
else:
    n = (n + 1) * 5

if n >= 25:
    n = n // 3 + 1
else:
    n = (n + 4) // 2 + 2

for z in range(0, 3):
    print(n)
    if n < 13 or n == 14:
        n = n + z
        if z >= 1:
            x = x + 1
            y = y + 3
        else:
            x = x + 2
    else:
        if z > 0:
            x = 7
        x = z + 2
    
    n = n + x + y

print("n inicial=", n_ini)
print("n final=", n)