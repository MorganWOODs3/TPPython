n = float(input("Tapez la valeur de n : "))
print("La table de multiplication de : ", n," est :")
for i in range(0,10):
    o=[i,n,round(i*n, 2)]
    print(f"{n} x  {i} = ",o[2])
