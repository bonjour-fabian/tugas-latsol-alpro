def cek_prima(x):
    faktor = 0
    prima = True
    for i in range(1, x+1):
        if x % i == 0:
            faktor+=1
    if faktor != 2:
        prima = False
    return prima

n = int(input("bilangan = "))
print(cek_prima(n))