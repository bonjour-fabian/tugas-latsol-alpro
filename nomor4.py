def non_rekursif(n):
    y=0
    for i in range(1, n+1):
        y+=2*i
    return y

def rekursif(n):
    if n > 0:
        y = 2 * n
        return y + rekursif(n-1)
    else:
        return 0

print(non_rekursif(3))
print(rekursif(3))