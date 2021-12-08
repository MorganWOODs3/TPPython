t = int(input('Entrer un nombre : '))
def factorielle(n):
    fact = 1
    for i in range (1,n+1):
        fact= i*factorielle(n-1)
    return(fact)
print("La factorisation", t, "est", factorielle(t))