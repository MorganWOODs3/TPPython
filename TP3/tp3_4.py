def factorielle(n):
    fact = 1
    for i in range (1,n+1):
        fact= i*factorielle(n-1)
    return (fact)

def factorielle(n):
    fact = 1
    i = 2
    while (i <= n):
        fact = i * factorielle(n - 1)
        i = i + 1
    return (fact)

variable=int(input('Choisiser votre variable 1 = range et 2 = While : '))

if variable==1:
    x = int(input('Variable (range) entrer un nombre : '))
    print("La factorisation", x, "est", factorielle(x))

else:
    t = int(input('Variable (while) entrer un nombre : '))
    print("La factorisation", t, "est", factorielle(t))


