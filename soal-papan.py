def faktorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * faktorial(n-1)

n = int(input("n = "))
y = 0

for i in range(1, n+1):
    if i % 2 == 0:
        y-=1/faktorial(i)
    else:
        y+=faktorial(i)

print(f"{y:.2f}")