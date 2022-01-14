

n = int(input("quel est la racine carré de ce nombre: "))
nMin = n - 0.001
nMax = n + 0.001
a= n/2
resultat= a*a

#Ne marche pas
while nMin > resultat or resultat > nMax:
    if resultat > nMax:
        a = (a/2)
        resultat= a*a
    elif resultat < nMin:
        a= ((a + (a/2))/2)
        resultat= a*a
print("le resultat est " + str(resultat))