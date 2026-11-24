n = int(input("n = "))

#nomor 1
S = 0
for i in range(1,n+1):
    S+=1/i

print(f"\n {S:.4f} \n")

#nomor 2
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()